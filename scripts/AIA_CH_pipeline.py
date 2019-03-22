#!/usr/bin/env python3
import sys
import logging
import argparse
from datetime import datetime, timedelta
from AIA_CH_spoca_jobs import run_spoca_jobs
from AIA_CH_submit_events import submit_CHMap_events
from event_db import EventDB

def parse_date(date_string):
	# TODO replace with fromisoformat when migrating to python 3.7
	for date_format in '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M', '%Y-%m-%dT%H', '%Y-%m-%d':
		try:
			result = datetime.strptime(date_string, date_format)
		except ValueError:
			pass
		else:
			break
	else:
		raise ValueError('Could not parse date string to datetime')
	
	return result

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run the pipeline to create CH maps, track them, extract the events from them, and submit those events')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-20', type=parse_date, help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', default = datetime.utcnow().strftime('%Y-%m-%d'), type=parse_date, help = 'End date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--do_not_submit', action='store_true', help = 'If set, the events will not be submitted')
	parser.add_argument('--untracked_maps', '-u', metavar = 'MAP', nargs='*', help = 'File paths of not yet tracked CH maps')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Run the spoca jobs
	try:
		CH_maps = run_spoca_jobs(args.start_date, args.end_date, untracked_maps = args.untracked_maps)
	except Exception as why:
		logging.critical(str(why))
		sys.exit(1)
	
	# Instantiate the EventDB
	event_db = EventDB()
	
	if not args.do_not_submit:
		# Submit the events from the CH maps to the Event DB
		for CH_map in CH_maps:
			submit_CHMap_events(CH_map, event_db)
