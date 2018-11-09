#!/usr/bin/env python3
import os
import subprocess
import logging
import argparse
from glob import glob
from datetime import datetime, timedelta
from spoca_job import Job, JobError
from AIA_quality import get_quality, get_quality_errors
from AIA_CH_event import get_CHMap_events, merge_spoca_coronal_hole, write_events
from eventdb import EventDB, EventDBError

# Path to the classification program
classification_exec = '/home/rwceventdb/SPoCA/bin/classification.x'

# Path to the classification program config file
classification_config_file = '/home/rwceventdb/scripts/AIA_CH_classification.config'

# Path to the centers file
classification_centers_file = '/home/rwceventdb/CH_maps/centers.txt'

# The frequency to run the classification program
classification_run_frequency = timedelta(hours = 4)

# Path to the get_CH_map program
get_CH_map_exec = '/home/rwceventdb/SPoCA/bin/get_CH_map.x'

# Path to the get_CH_map program config file
get_CH_map_config_file = '/home/rwceventdb/scripts/AIA_CH_get_CH_map.config'

# Path to the tracking program
tracking_exec = '/home/rwceventdb/SPoCA/bin/tracking.x'

# Path to the tracking program config file
tracking_config_file = '/home/rwceventdb/scripts/AIA_CH_tracking.config'

# The minimum number of files that overlaps with the previous tracking (see maxDeltaT)
tracking_overlap = 6

# The number of CH maps to run the tracking program on
tracking_run_count = 6

# Directory to output the maps
maps_directory = '/home/rwceventdb/CH_maps/'

# Directory to output the stats
stats_directory = '/home/rwceventdb/CH_stats/'

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Wavelengths for spoca
wavelengths = [193]

# The max time that must be waited before processing data
max_delay = timedelta(days = 16)


def date_range(start, end, step):
	'''Equivalent to range for date'''
	date = start.replace()
	while date < end:
		yield date
		date += step

def get_AIA_files(date, wavelengths):
	# Find the AIA files for the given date, wavelengths and required quality
	file_paths = dict()
	
	for wavelength in wavelengths:
		for file_path in sorted(glob(aia_file_pattern.format(date=date, wavelength=wavelength))):
			quality = get_quality(file_path)
			# A quality of 0 means no defect
			if quality == 0:
				file_paths[wavelength] = file_path
				break
			else:
				logging.info('Skipping file %s with bad quality: %s', file_path, get_quality_errors(quality))
	
	return file_paths

# Create a classification job with the appropriate parameters
classification = Job(classification_exec, config = classification_config_file, centersFile = classification_centers_file)

def create_segmented_map(AIA_images, date):
	# File path for the Segmented map
	segmented_map = os.path.join(maps_directory, date.strftime('%Y%m%d_%H%M%S') + '.SegmentedMap.fits')
	
	# We run the classification program
	logging.debug('Running classification job:\n%s', ' '.join(classification.get_command(*AIA_images, output = segmented_map)))
	return_code, output, error = classification(*AIA_images, output = segmented_map)
	
	# We check if the program ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'classification', AIA_images = AIA_images)
	elif not os.path.exists(segmented_map):
		raise JobError(message = 'Could not find output file {segmented_map}', segmented_map = segmented_map)
	else:
		logging.info('classification job on files "%s" ran without errors', ' '.join(AIA_images))
	
	return segmented_map

# Create a get_CH_map job with the appropriate parameters
get_CH_map = Job(get_CH_map_exec, config = get_CH_map_config_file)

def create_CH_map(segmented_map, date, images):
	# File path for the CH map
	CH_map = os.path.join(maps_directory, date.strftime('%Y%m%d_%H%M%S') + '.CHMap.fits')
	
	# We run the get_CH_map program
	logging.debug('Running get_CH_map job:\n%s', ' '.join(get_CH_map.get_command(segmented_map, *images, output = CH_map)))
	return_code, output, error = get_CH_map(segmented_map, *images, output = CH_map)
	
	# We check if the program ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'get_CH_map', segmented_map = segmented_map)
	elif not os.path.exists(CH_map):
		raise JobError(message = 'Could not find output file {CH_map}', CH_map = CH_map)
	else:
		logging.info('get_CH_map job on file "%s" ran without errors', segmented_map)
	
	return CH_map


# Create a tracking job with the appropriate parameters
tracking = Job(tracking_exec, config = tracking_config_file, maxDeltaT = (tracking_overlap * classification_run_frequency).total_seconds())

def track_CH_maps(CH_maps):
	logging.debug('Running tracking job:\n%s', ' '.join(tracking.get_command(*CH_maps)))
	return_code, output, error = tracking(*CH_maps)
	
	# We check if the program ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'tracking', CH_maps = CH_maps)
	else:
		logging.info('tracking job on files "%s" ran without errors\n%s', ' '.join(CH_maps), output)


def create_event(event_type, event):
	
	# Check if the event has already been submitted to the EventDB before
	try:
		result = eventdb.get_event(event_type, event['name'])
	except LookupError as why:
		# The event does not exists
		already_submitted = False
	else:
		already_submitted = True
		logging.warning('Trying to submit previously submitted event "%s"', event['name'])
	
	if not already_submitted:
		result = eventdb.submit_event(event)
		logging.info('Succesfully submitted event "%s" (%s)', event['name'], result)


def update_event(event_type, event, merge_events):
	
	# Check if the event has already been submitted to the EventDB before
	try:
		previous_event = eventdb.get_event(event_type, event['name'])
	except LookupError as why:
		# The event does not exists
		pass
	else:
		# The event needs to be updated
		logging.info('Updating event "%s"', event['name'])
		event = merge_events(event, previous_event)
		
	result = eventdb.submit_event(event)
	logging.info('Succesfully submitted event "%s" (%s)', event['name'], result)


def submit_events(CH_map):
	
	# Extract the events from the CH_map
	map_events = get_CHMap_events(CH_map)
	
	for name, events in map_events.items():
		
		# Create the SPOCA_CoronalHoleDetection event
		try:
			create_event('SPOCA_CoronalHoleDetection', events['spoca_coronal_hole_detection'])
		except EventDBError as why:
			logging.error('Failed to submit event "%s": %s', events['spoca_coronal_hole_detection']['name'], why)
			# If we fail, we must not submit the other events dependent on the SPOCA_CoronalHoleDetection event
			continue
		
		# Create the SPOCA_CoronalHoleDetectionStatistics events
		for event in events['spoca_coronal_hole_detection_statistics']:
			try:
				create_event('SPOCA_CoronalHoleDetectionStatistics', event)
			except EventDBError as why:
				logging.error('Failed to submit event "%s": %s', event['name'], why)
		
		# Create or update the SPOCA_CoronalHole event
		try:
			update_event('SPOCA_CoronalHole', events['spoca_coronal_hole'], merge_events = merge_spoca_coronal_hole)
		except EventDBError as why:
			logging.error('Failed to submit event "%s": %s', name, why)


def main(start_date, end_date):
	
	# Find the CH maps already created
	CH_maps = sorted(glob(os.path.join(maps_directory, '*' + '.CHMap.fits')))[-2 * tracking_overlap:]
	
	# Start the loop
	for date in date_range(start_date, end_date, classification_run_frequency):
		
		# Get the AIA files for the classification
		file_paths = get_AIA_files(date, wavelengths)
		
		# Check if we have all the files we need
		if not all(w in file_paths for w in wavelengths):
			logging.info('Missing AIA files for date %s', date)
			
			# If max_delay has passed, then we continue, else we stop and wait
			if datetime.now() - date >= max_delay:
				logging.warning('Max delay %s was passed, skipping missing files' % max_delay)
				continue
			else:
				logging.info('Max delay %s was not passed, waiting missing files' % max_delay)
				break
		
		# Make the list of AIA images
		AIA_images = [file_paths[w] for w in wavelengths]
		
		# Create the Segmented map
		segmented_map = create_segmented_map(AIA_images, date)
			
		# Create the CH map
		CH_map = create_CH_map(segmented_map, date, AIA_images)
		
		# We add the CH map to the list of CH maps
		CH_maps.append(CH_map)
		
		# If we have enough CH maps, we run the tracking program
		if len(CH_maps) >= tracking_overlap + tracking_run_count:
			track_CH_maps(CH_maps)
			
			# Keep only the CH maps needed for the overlap
			CH_maps = CH_maps[-tracking_overlap:]
			
			# We submit the events from the CH maps
			for CH_map in CH_maps:
				submit_events(CH_map)
			
		else:
			logging.debug('Not enough maps to run tracking, need %s but have only %s', tracking_run_count, len(CH_maps))

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run SPoCA to extract CH maps from AIA 193A fits files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-20', help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', help = 'End date of AIA files to process, in form YYYY-MM-DD')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Parse the start and end date
	start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
	end_date = datetime.strptime(args.end_date, '%Y-%m-%d') if args.end_date else datetime.utcnow()
	
	# Instantiate the EventDB
	eventdb = EventDB()
	
	try:
		main(start_date, end_date)
	except Exception as why:
		logging.critical(str(why))
