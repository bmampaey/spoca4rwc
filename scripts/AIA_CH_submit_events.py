#!/usr/bin/env python3
import os
import logging
import argparse
from AIA_CH_event import get_CHMap_events, merge_spoca_coronal_hole, save_CHMap_events
from event_db import EventDB, EventDBError

def submit_CHMap_events(map_path, event_db):
	'''Extract the events from a CHMap, save them to disk and submit them to the Event DB'''
	
	# Extract the events from the CH map
	run_event, CH_events = get_CHMap_events(map_path)
	
	# Save the events to disk to a subdirectory based on the name of the CH_map
	save_CHMap_events(run_event, CH_events, os.path.basename(map_path).split('.')[0])
	
	# Submit the events to the Event db
	for events in CH_events:
		
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
			if event['data']['PixelsNumber'] > 0:
				try:
					event_db.create_event(event)
				except EventDBError as why:
					logging.error('Failed to submit event "%s": %s', event['name'], why)
			else:
				logging.warning('SPOCA_CoronalHoleStatistics event "%s" has PixelsNumber <=0, skipping!', event)
		
		# Create or update the SPOCA_CoronalHole event
		try:
			event_db.update_event(events['spoca_coronal_hole'], merge_events = merge_spoca_coronal_hole)
		except EventDBError as why:
			logging.error('Failed to submit event "%s": %s', events['spoca_coronal_hole']['name'], why)
	
	# Create the SPOCA_CoronalHoleRun event
	try:
		event_db.create_event(run_event)
	except EventDBError as why:
		logging.error('Failed to submit event "%s": %s', run_event['name'], why)


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CHMap and submit them')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The file path to a tracked SPoCA CHMap')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Instantiate the EventDB
	event_db = EventDB()
	
	# Submit the events from the CH maps to the Event DB
	for map_path in args.maps:
		logging.info('Parsing map %s', map_path)
		submit_CHMap_events(map_path, event_db)
