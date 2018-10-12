#!/usr/bin/env python3
import os, sys
import subprocess
import logging
import argparse
import glob
from datetime import datetime, timedelta
from spoca_job import Classification, Tracking
from test_quality import get_quality, get_quality_errors

# Path to the classification program
classification_exec = '/home/rwceventdb/SPoCA/bin1/classification.x'

# Path to the classification program config file
classification_config_file = '/home/rwceventdb/scripts/AIA_CH.segmentation.config'

# Path to the centers file
classification_centers_file = '/home/rwceventdb/CH_maps/centers.txt'

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
log_file =  '/home/rwceventdb/log/run_spoca_CH.log'

# Start point of the script
if __name__ == '__main__':
	
	script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
	
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
	
	# Create a classification job with the parameters
	classification = Classification(classification_exec, classification_config_file, kwargs = {'centersFile': classification_centers_file})
	
	# Test the classification  parameters
	result, output = classification.test_parameters()
	if result:
		logging.debug('classification parameters in file %s seem GOOD', classification_config_file)
		logging.debug(output)
	else:
		logging.warning('classification parameters in file %s could be BAD', classification_config_file)
		logging.warning(output)
	
	# Set the start and end date
	start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
	end_date = datetime.strptime(args.end_date, '%Y-%m-%d') if args.end_date else datetime.utcnow()
	
	# Start the loop
	while start_date < end_date:
		
		# Find the AIA files we need
		file_paths = dict()
		for wavelength in wavelengths:
			for file_path in sorted(glob.glob(aia_file_pattern.format(date=start_date, wavelength=wavelength))):
				quality = get_quality(file_path)
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
		
		# We run the classification program
		logging.debug('Running classification job:\n%s %s', classification, ' '.join(file_paths[w] for w in wavelengths))
		
		map_name = start_date.strftime('%Y%m%d_%H%M%S')
		
		return_code, output, error = classification(args = [file_paths[w] for w in wavelengths], kwargs = {'outputDirectory': os.path.join(maps_directory, map_name)})
		
		# We check if program ran succesfully
		if return_code != 0:
			logging.error('Classification job on files "%s" ran with error\nReturn code: %s\nOutput: %s\nError: %s', job, ' '.join(file_paths[w] for w in wavelengths), return_code, output, error)
		else:
			logging.info('Classification job on files "%s" ran without errors', ' '.join(file_paths[w] for w in wavelengths))
			
			# Get the map file
			map_file_path = os.path.join(maps_directory, map_name + '.CHMap.fits')
			if not os.path.exists(map_file_path):
				logging.error('Could not find map file %s', map_file_path)
				break
		
		# We update the start_date for the next run
		start_date += run_frequency
