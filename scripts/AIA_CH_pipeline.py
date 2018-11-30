#!/usr/bin/env python3
import os
import sys
import logging
import argparse
from datetime import datetime
from AIA_CH_spoca_jobs import run_spoca_jobs
from AIA_CH_event import get_CHMap_events, merge_spoca_coronal_hole, save_CHMap_events
from event_db import EventDB, EventDBError

def submit_CHMap_events(CH_map, event_db):
	'''Extract the events from a CHMap, save them to disk and submit them to the Event DB'''
	
	# Extract the events from the CH map
	run_event, CH_events = get_CHMap_events(CH_map)
	
	# Save the events to disk to a subdirectory based on the name of the CH_map
	save_CHMap_events(run_event, CH_events, os.path.basename(CH_map).split('.')[0])
	
	# Submit the events to the Event db
	for name, events in CH_events.items():
		
		# Create the SPOCA_CoronalHoleDetection event
		try:
			event_db.create_event(events['spoca_coronal_hole_detection'])
		except EventDBError as why:
			logging.error('Failed to submit event "%s": %s', events['spoca_coronal_hole_detection']['name'], why)
			# If we fail, we must not submit an other event dependent on the SPOCA_CoronalHoleDetection event
			# So we modify the SPOCA_CoronalHoleRun event, and skip the SPOCA_CoronalHole and SPOCA_CoronalHoleStatistics
			run_event['data']['detections'].remove(events['spoca_coronal_hole_detection']['name'])
			continue
		
		# Create the SPOCA_CoronalHoleStatistics events
		for event in events['spoca_coronal_hole_statistics']:
			try:
				event_db.create_event(event)
			except EventDBError as why:
				logging.error('Failed to submit event "%s": %s', event['name'], why)
		
		# Create or update the SPOCA_CoronalHole event
		try:
			event_db.update_event(events['spoca_coronal_hole'], merge_events = merge_spoca_coronal_hole)
		except EventDBError as why:
			logging.error('Failed to submit event "%s": %s', name, why)
		
	# Create the SPOCA_CoronalHoleRun event
	event_db.create_event(run_event)


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Run the pipeline to create CH maps, track them, extract the events from them, and submit those events')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--start_date', '-s', default = '2010-05-20', help = 'Start date of AIA files, in form YYYY-MM-DD')
	parser.add_argument('--end_date', '-e', default = datetime.utcnow().strftime('%Y-%m-%d'), help = 'End date of AIA files, in form YYYY-MM-DD')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Parse the start and end date
	start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
	end_date = datetime.strptime(args.end_date, '%Y-%m-%d')
	
	# Run the spoca jobs
	try:
		CH_maps = run_spoca_jobs(start_date, end_date)
	except Exception as why:
		logging.critical(str(why))
		sys.exit(1)
	
	# Instantiate the EventDB
	event_db = EventDB()
	
	# Submit the events from the CH maps to the Event DB
	for CH_map in CH_maps:
		submit_CHMap_events(CH_map, event_db)
