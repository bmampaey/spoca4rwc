#!/usr/bin/env python3
import os
import subprocess
import logging
import argparse
import glob
from datetime import datetime, timedelta
from spoca_job import Job
from AIA_quality import get_quality, get_quality_errors

# Path to the classification program
classification_exec = '/home/rwceventdb/SPoCA/bin/classification.x'

# Path to the classification program config file
classification_config_file = '/home/rwceventdb/scripts/AIA_CH.classification.config'

# Path to the centers file
classification_centers_file = '/home/rwceventdb/CH_maps/centers.txt'

# Path to the get_CH_map program
get_CH_map_exec = '/home/rwceventdb/SPoCA/bin/get_CH_map.x'

# Path to the get_CH_map program config file
get_CH_map_config_file = '/home/rwceventdb/scripts/AIA_CH.get_CH_map.config'

# Path to the tracking program
tracking_exec = '/home/rwceventdb/SPoCA/bin/tracking.x'

# Path to the tracking program config file
tracking_config_file = '/home/rwceventdb/scripts/AIA_CH.tracking.config'

# Directory to output the maps
maps_directory = '/home/rwceventdb/CH_maps/'

# Directory to output the stats
stats_directory = '/home/rwceventdb/CH_stats/'

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Wavelengths for spoca
wavelengths = [193]

# The frequency to run the classification program
run_frequency = timedelta(hours = 4)

# The max time that must be waited before processing data
max_delay = timedelta(days = 16)

# Default path for the log file
log_file =  '/home/rwceventdb/log/AIA_CH.run_spoca_jobs.log'

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run SPoCA to extract CH maps from AIA 193A fits files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', default = log_file, help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-20', help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', help = 'End date of AIA files to process, in form YYYY-MM-DD')
	args = parser.parse_args()
	
	# Setup the logging
	if args.debug:
		logging.basicConfig(level = logging.DEBUG, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	
	# Create a classification job with the appropriate parameters
	classification = Job(classification_exec, config = classification_config_file, centersFile = classification_centers_file)
	
	# Create a get_CH_map job with the appropriate parameters
	get_CH_map = Job(get_CH_map_exec, config = get_CH_map_config_file)
	
	# Create a tracking job with the appropriate parameters
	tracking = Job(tracking_exec, config = tracking_config_file)
	
	# Set the start and end date
	start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
	end_date = datetime.strptime(args.end_date, '%Y-%m-%d') if args.end_date else datetime.utcnow()
	
	# Start the loop
	while start_date < end_date:
		
		# Find the AIA files for the given date, wavelengths and required quality
		file_paths = dict()
		for wavelength in wavelengths:
			for file_path in sorted(glob.glob(aia_file_pattern.format(date=start_date, wavelength=wavelength))):
				quality = get_quality(file_path)
				# A quality of 0 means no defect
				if quality == 0:
					file_paths[wavelength] = file_path
					break
				else:
					logging.info('Skipping file %s with bad quality: %s', file_path, get_quality_errors(quality))
		
		# Check if we have all the files we need
		if not all(w in file_paths for w in wavelengths):
			logging.info('Missing AIA files for date %s', start_date)
			
			# If max_delay has passed, then we continue, else we stop and wait
			if datetime.now() - start_date >= max_delay:
				logging.warning('Max delay %s was passed, skipping missing files' % max_delay)
				continue
			else:
				logging.info('Max delay %s was not passed, waiting missing files' % max_delay)
				break
		else:
			# Flatten the file paths
			file_paths = [file_paths[w] for w in wavelengths]
		
		# We run the classification program
		logging.debug('Running classification job:\n%s %s', classification, ' '.join(file_paths))
		
		segmented_map_path = os.path.join(maps_directory, start_date.strftime('%Y%m%d_%H%M%S') + '.SegmentedMap.fits')
		
		return_code, output, error = classification(*file_paths, output = segmented_map_path)
		
		# We check if program ran succesfully
		if return_code != 0:
			logging.error('classification job on files "%s" ran with error\nReturn code: %s\nOutput: %s\nError: %s', ' '.join(file_paths), return_code, output, error)
			break
		elif not os.path.exists(segmented_map_path):
			logging.error('Could not find output file %s', segmented_map_path)
			break
		else:
			logging.info('classification job on files "%s" ran without errors', ' '.join(file_paths))
			
		
		# We run the get_CH_map program
		logging.debug('Running get_CH_map job:\n%s %s', get_CH_map, segmented_map_path)
		
		CH_map_path = os.path.join(maps_directory, start_date.strftime('%Y%m%d_%H%M%S') + '.CHdMap.fits')
		
		return_code, output, error = get_CH_map(segmented_map_path, output = CH_map_path)
		
		# We check if program ran succesfully
		if return_code != 0:
			logging.error('get_CH_map job on file "%s" ran with error\nReturn code: %s\nOutput: %s\nError: %s', segmented_map_path, return_code, output, error)
			break
		elif not os.path.exists(segmented_map_path):
			logging.error('Could not find output file %s', CH_map_path)
			break
		else:
			logging.info('get_CH_map job on files "%s" ran without errors', segmented_map_path)
		
		# We update the start_date for the next run
		start_date += run_frequency
