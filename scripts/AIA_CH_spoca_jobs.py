#!/usr/bin/env python3
import os
import sys
import logging
import argparse
from glob import glob
from datetime import datetime, timedelta
from job import Job, JobError
from AIA_quality import get_quality, get_quality_errors


# Path to the classification program
classification_exec = '/home/rwceventdb/SPoCA/bin/classification.x'

# Path to the classification program config file
classification_config_file = '/home/rwceventdb/scripts/AIA_CH_classification.config'

# Path to the centers file
classification_centers_file = '/data/RWC/SPoCA_v2/CH_maps/centers.txt'

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

# Path to the tracking color file
tracking_color_file = '/data/RWC/SPoCA_v2/CH_maps/tracking_color.txt'

# The minimum number of files that overlaps with the previous tracking (see maxDeltaT)
tracking_overlap = 6

# The number of CH maps to run the tracking program on
tracking_run_count = 3

# Directory to output the maps
maps_directory = '/data/RWC/SPoCA_v2/CH_maps/'

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_quicklook/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/H{date.hour:02d}00/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Directory where the prepped HMI files are located
hmi_file_pattern = '/data/SDO/public/HMI_quicklook/magnetogram/{date.year:04d}/{date.month:02d}/{date.day:02d}/HMI.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.*.fits'

# Wavelengths of AIA data to run the classification program on
AIA_wavelengths = [193]

def date_range(start, end, step):
	'''Equivalent to range for date'''
	date = start.replace()
	while date < end:
		yield date
		date += step

def parse_tracking_color_file(tracking_color_file):
	try:
		with open(tracking_color_file, 'tr') as f:
			text = f.readline()
		last_color = int(text.split(':')[1])
	except Exception as why:
		logging.warning('Could not read tracking color from file "%s": %s', tracking_color_file, why)
		return 0
	else:
		logging.debug('Found last color %s from file %s', last_color, tracking_color_file)
		return last_color

def get_good_file(file_pattern, ignore_bits = None):
	'''Return the first file that matches the file_pattern and has a good quality'''
	
	for file_path in sorted(glob(file_pattern)):
		
		# Get the quality of the file
		if ignore_bits is None:
			quality = get_quality(file_path)
		else:
			quality = get_quality(file_path, ignore_bits)
		
		# A quality of 0 means no defect
		if quality == 0:
			return file_path
		else:
			logging.info('Skipping file %s with bad quality: %s', file_path, get_quality_errors(quality))


def get_AIA_files(date, wavelengths):
	'''Return a list of AIA files for the specified date and wavelengths'''
	
	file_paths = list()
	
	for wavelength in wavelengths:
		
		file_path = get_good_file(aia_file_pattern.format(date=date, wavelength=wavelength))
		
		if file_path is None:
			raise FileNotFoundError('AIA file for date %s and wavelength %s was not found' % (date, wavelengths))
		else:
			file_paths.append(file_path)

	return file_paths

def get_HMI_files(date):
	'''Return a list of HMI files for the specified date'''
	
	file_path = get_good_file(hmi_file_pattern.format(date=date))
	
	if file_path is None:
		raise FileNotFoundError('HMI file for date %s was not found' % date)
	else:
		return [file_path]


def create_segmented_map(AIA_images, date):
	'''Run the classification program'''
	
	# File path for the Segmented map to create
	segmented_map = os.path.join(maps_directory, date.strftime('%Y%m%d_%H%M%S') + '.SegmentedMap.fits')
	
	# Create a job for the classification program with the appropriate parameters
	job = Job(classification_exec, *AIA_images, config = classification_config_file, centersFile = classification_centers_file, output = segmented_map)
	
	logging.info('Running job\n%s', job)
	
	# Run the classification job
	return_code, output, error = job()
	
	# Check if the job ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'classification', AIA_images = AIA_images)
	elif not os.path.exists(segmented_map):
		raise JobError(message = 'Could not find output file {segmented_map}', segmented_map = segmented_map)
	else:
		logging.debug('Job ran without errors, output: %s', output)
	
	return segmented_map


def create_CH_map(segmented_map, date, images):
	'''Run the get_CH_map program'''
	
	# File path for the CH map to create
	CH_map = os.path.join(maps_directory, date.strftime('%Y%m%d_%H%M%S') + '.CHMap.fits')
	
	# Create a job for the get_CH_map program with the appropriate parameters
	job = Job(get_CH_map_exec, segmented_map, *images, config = get_CH_map_config_file, output = CH_map)
	
	logging.info('Running job\n%s', job)
	
	# Run the get_CH_map job
	return_code, output, error = job()
	
	# Check if the job ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'get_CH_map', segmented_map = segmented_map)
	elif not os.path.exists(CH_map):
		raise JobError(message = 'Could not find output file {CH_map}', CH_map = CH_map)
	else:
		logging.debug('Job ran without errors, output: %s', output)
	
	return CH_map


def track_maps(tracked_maps, untracked_maps, newly_tracked_maps):
	'''Run the tracking program'''
	
	# File paths of the maps to run the tracking on
	maps = tracked_maps[-tracking_overlap:] + untracked_maps
	
	# last color of the previous tracking
	last_color = parse_tracking_color_file(tracking_color_file)
	
	# Create a job for the tracking program with the appropriate parameters
	job = Job(tracking_exec, *maps, config = tracking_config_file, maxDeltaT = (tracking_overlap * classification_run_frequency).total_seconds(), newColor = last_color)
	
	logging.info('Running job\n%s', job)
	
	# Run the tracking job
	return_code, output, error = job()
	
	# Check if the job ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'tracking', maps = maps)
	else:
		logging.debug('Job ran without errors, output: %s', output)
		try:
			with open(tracking_color_file, 'tw') as f:
				f.write(output)
		except Exception as why:
			logging.error('Could not write tracking color to file "%s": %s', tracking_color_file, why)
	
	return tracked_maps + untracked_maps, [], newly_tracked_maps + untracked_maps


def run_spoca_jobs(start_date, end_date, tracked_maps = None, untracked_maps = None):
	'''Run the SPoCA jobs to create and track the CHMaps'''
	
	# If no tracked maps were given, we assumed all existing are
	if tracked_maps is None:
		tracked_maps = sorted(glob(os.path.join(maps_directory, '*.CHMap.fits')))
	
	# If no untracked maps were given, we assume none are
	if untracked_maps is None:
		untracked_maps = list()
	else:
		# We need to remove the untracked maps from the tracked maps
		for untracked_map in untracked_maps:
			tracked_maps = list(filter(lambda tracked_map: not os.path.samefile(tracked_map, untracked_map), tracked_maps))
		
	
	# We will return the list of all newly tracked maps
	newly_tracked_maps = list()
	
	# Start the loop
	for date in date_range(start_date, end_date, classification_run_frequency):
		
		# Get the AIA files for the classification
		try:
			AIA_images = get_AIA_files(date, AIA_wavelengths)
		except FileNotFoundError as why:
			logging.warning('Missing AIA files for date %s, skipping missing files!', date)
		
		# Get the list of HMI images
		try:
			HMI_images = get_HMI_files(date)
		except FileNotFoundError as why:
			# It's okay if HMI files are missing, we just won't have HMI stats for the CH
			HMI_images = list()
		
		# Create the Segmented map
		segmented_map = create_segmented_map(AIA_images, date)
		
		# Create the CH map
		CH_map = create_CH_map(segmented_map, date, AIA_images + HMI_images)
		
		# Add the CH map to the list of untracked maps
		untracked_maps.append(CH_map)
		
		# If we have enough untracked maps, we run the tracking program
		if len(untracked_maps) >= tracking_run_count:
			tracked_maps, untracked_maps, newly_tracked_maps = track_maps(tracked_maps, untracked_maps, newly_tracked_maps)
		else:
			logging.debug('Not enough maps to run tracking, need %s but have only %s', tracking_run_count, len(untracked_maps))
	
	# Track the remaing untracked maps
	if untracked_maps:
		tracked_maps, untracked_maps, newly_tracked_maps = track_maps(tracked_maps, untracked_maps, newly_tracked_maps)
	
	return newly_tracked_maps


# Start point of the script
if __name__ == '__main__':

	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Create and track CH maps')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-20', help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', default = datetime.utcnow().strftime('%Y-%m-%d'), help = 'End date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--tracked_maps', '-t', metavar = 'MAP', nargs='*', help = 'File paths of previously tracked CH maps')
	parser.add_argument('--untracked_maps', '-u', metavar = 'MAP', nargs='*', help = 'File paths of not yet tracked CH maps')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Parse the start and end date
	start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
	end_date = datetime.strptime(args.end_date, '%Y-%m-%d') if args.end_date else datetime.utcnow()
	
	# Run the SPoCA jobs
	try:
		CH_maps = run_spoca_jobs(start_date, end_date, args.tracked_maps, args.untracked_maps)
	except Exception as why:
		logging.critical(str(why))
		sys.exit(1)
