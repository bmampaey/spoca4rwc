#!/usr/bin/env python3
import os, sys
import subprocess
import logging
import argparse
import glob
from datetime import datetime, timedelta
from spoca_job import Classification, Tracking
from test_quality import get_quality, get_quality_errors

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Path to the spoca classification program
spoca_bin = '/home/rwceventdb/SPoCA/bin1/classification.x'

# Path to the config of spoca classification program
spoca_config = '/home/rwceventdb/AIA/AIA_CH.segmentation.config'

# Wavelengths for spoca
wavelengths = [193]

# Directory to output the maps
maps_directory = '/home/rwceventdb/CH_maps/'

# Directory to output the stats
stats_directory = '/home/rwceventdb/CH_stats/'

# The times of day to run SPoCA
run_frequency = timedelta(hours = 4)

# The max time that must be waited before processing data
max_delay = timedelta(days = 16)

# Default path for the log file
log_file =  '/home/rwceventdb/logs/run_spoca_CH.log'


def setup_spoca(spoca_bin, configfile, output_dir):
	
	class segmentation_instance(segmentation):
		pass
	
	segmentation_instance.set_parameters(configfile, output_dir)
	segmentation_instance.bin = spoca_bin
	ok, reason = segmentation_instance.test_parameters()
	if ok:
		logging.info('Spoca parameters in file %s seem ok', configfile)
		logging.debug(reason)
	else:
		logging.warning('Spoca parameters in file %s could be wrong', configfile)
		logging.warning(reason)
	
	return segmentation_instance


def run_spoca(spoca, fitsfiles, name):
	
	logging.info('Running spoca on files %s', fitsfiles)
	spoca_command = [spoca.bin] + spoca.build_arguments(fitsfiles, name)
	spoca_process = subprocess.Popen(spoca_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, errors = spoca_process.communicate()
	if spoca_process.returncode == 0:
		logging.debug('Sucessfully ran spoca command %s, output: %s, errors: %s', ' '.join(spoca_command), str(output), str(errors))
		return True
	else:
		logging.error('Error running spoca command %s, output: %s, errors: %s', ' '.join(spoca_command), str(output), str(errors))
		return False

# Start point of the script
if __name__ == '__main__':
	
	script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run SPoCA to extract CH maps from AIA 193A fits files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', default = log_file, help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-13', help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', help = 'End date of AIA files to process, in form YYYY-MM-DD')
	args = parser.parse_args()
	
	# Setup the logging
	if args.debug:
		logging.basicConfig(level = logging.DEBUG, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	
	# Create a classification job with the parameters
	classification = Classification(spoca_bin, spoca_config, kwargs = {'outputDirectory': maps_directory})
	
	# Test the classification  parameters
	result, output = classification.test_parameters()
	if result:
		logging.debug('classification parameters in file %s seem GOOD', configfile)
		logging.debug(output)
	else:
		logging.warning('classification parameters in file %s could be BAD', configfile)
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
			else:
				logging.info('Max delay %s was not passed, waiting missing files' % max_delay)
				break
		
		map_name = start_date.strftime('%Y%m%d_%H%M%S')
		
		# We run spoca
		run_success = run_spoca(spoca, [file_paths[w] for w in wavelengths], map_name)
		
		# We check if the CH map exists
		if run_success:
			CH_map = os.path.join(maps_directory, map_name+'.SegmentedMap.fits')
			if not os.path.exists(CH_map):
				logging.error('Could not find CH_map %s', CH_map)
				break
		
		# We update the start_date for the next run
		start_date += run_frequency
