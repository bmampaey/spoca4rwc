#!/usr/bin/env python3
import os
import logging
import argparse
from glob import glob
from datetime import datetime
from job import Job, JobError

# Path to the overlay program
overlay_exec = '/home/rwceventdb/SPoCA/bin/overlay.x'

# Path to the overlay program config file
overlay_config_file = '/home/rwceventdb/scripts/AIA_CH_overlay.config'

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Directory where the prepped HMI files are located
hmi_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/hmi.m_45s.prepped/{date.year:04d}/{date.month:02d}/{date.day:02d}/HMI.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.*.fits'

# Wavelengths of AIA data to run the overlay program on
AIA_wavelengths = [193]

def get_images(date):
	'''Return AIA and HMI images for the specified date'''
	file_paths = list()
	
	for wavelength in AIA_wavelengths:
		file_paths.append(min(glob(aia_file_pattern.format(date=date, wavelength=wavelength))))
	
	file_paths.append(min(glob(hmi_file_pattern.format(date=date))))
	
	return file_paths

def create_overlays(map, output_directory):
	'''Run the overlay program'''
	
	# Get the images on which to overlay the CH map
	images = get_images(datetime.strptime(os.path.basename(map).split('.')[0], '%Y%m%d_%H%M%S'))
	
	# Create a job for the overlay program with the appropriate parameters
	job = Job(overlay_exec, map, *images, config = overlay_config_file, output = output_directory)
	
	logging.info('Running job\n%s', job)
	
	# Run the overlay job
	return_code, output, error = job()
	
	# Check if the job ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'overlay', segmented_map = segmented_map)
	elif not os.path.exists(map):
		raise JobError(message = 'Could not find output file {map}', map = map)
	else:
		logging.debug('Job ran without errors, output: %s', output)


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run overlay to plot CH maps over AIA and HMI images')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--output_directory', '-o', default = '.', help = 'The directory where to write the overlays')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The file path to a tracked SPoCA CHMap')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	try:
		for map in args.maps:
			create_overlays(map, args.output_directory)
	except Exception as why:
		logging.critical(str(why))
