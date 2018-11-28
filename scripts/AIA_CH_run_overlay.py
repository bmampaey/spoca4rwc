#!/usr/bin/env python3
import os
import subprocess
import logging
import argparse
from glob import glob
from datetime import datetime, timedelta
from spoca_job import Job, JobError

# Path to the overlay program
overlay_exec = '/home/rwceventdb/SPoCA/bin/overlay.x'

# Path to the overlay program config file
overlay_config_file = '/home/rwceventdb/scripts/AIA_CH_overlay.config'

# Directory to output the maps
maps_directory = '/data/RWC/SPoCA/CH_maps/'

# Directory where the prepped AIA files are located
aia_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/{wavelength:04d}/{date.year:04d}/{date.month:02d}/{date.day:02d}/AIA.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.{wavelength:04d}.*.fits'

# Directory where the prepped HMI files are located
hmi_file_pattern = '/data/SDO/public/AIA_HMI_1h_synoptic/hmi.m_45s.prepped/{date.year:04d}/{date.month:02d}/{date.day:02d}/HMI.{date.year:04d}{date.month:02d}{date.day:02d}_{date.hour:02d}*.*.fits'

# Wavelengths for spoca
wavelengths = [193]

def get_files(date, wavelengths):
	file_paths = list()
	
	for wavelength in wavelengths:
		file_paths.append(min(glob(aia_file_pattern.format(date=date, wavelength=wavelength))))
	
	file_paths.append(min(glob(hmi_file_pattern.format(date=date))))
	
	return file_paths

# Create a overlay job with the appropriate parameters
overlay = Job(overlay_exec, config = overlay_config_file)

def create_overlay(CH_map, images, output_directory = maps_directory):
	
	# We run the overlay program
	logging.debug('Running overlay job:\n%s', ' '.join(overlay.get_command(CH_map, *images, output = output_directory)))
	return_code, output, error = overlay(CH_map, *images, output = output_directory)
	
	# We check if the program ran succesfully
	if return_code != 0:
		raise JobError(return_code, output, error, job_name = 'overlay', CH_map = CH_map)
	else:
		logging.info('overlay job on file "%s" ran without errors', CH_map)

def main(CH_maps):
	
	# Start the loop
	for CH_map in CH_maps:
		date = datetime.strptime(os.path.basename(CH_map).split('.')[0], '%Y%m%d_%H%M%S')
		
		images = get_files(date, wavelengths)
		
		logging.info('Create overlay for CH Map %s', CH_map)
		create_overlay(CH_map, images)

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run overlay to plot CH maps over AIA 193A fits files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('CH_maps', metavar = 'CH_MAP', nargs='+', help = 'The file path to a CH map')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	try:
		main(args.CH_maps)
	except Exception as why:
		logging.critical(str(why))
