#!/usr/bin/env python3

import argparse
import requests
import json
import logging

eventdb_server = "http://solrwc2:8888/"

class EventDB:
	'''Class to manage POST and GET to the Event DB server'''
	
	def __init__(self, server = eventdb_server, timeout = 10):
		self.submit_address = server + 'message'
		self.get_address = server + 'aquery'
		self.timeout = timeout
	
	def submit_event(self, event = eventdb_server):
		r = requests.post(self.submit_address, json = event, timeout = self.timeout)
		if r.status_code != 200:
			logging.error('POST returned error %s "%s": %s', r.status_code, r.reason, r.text)
			r.raise_for_status()
		return r.json()
	
	def get_errors(self, response):
		if isinstance(response, dict) and 'error' in response:
			return [response['error']]
		elif isinstance(response, list):
			return [rec['error'] for rec in response if 'error' in rec]
		else:
			return []
	
	def get_event(self, event_type, event_name):
		params = {
			'return': event_type,
			'constraints': '{event_type}$name$eq${event_name}'.format(event_type = event_type, event_name = event_name),
		}
		
		r = requests.get(self.get_address, params = params, timeout = self.timeout)
		if r.status_code != 200:
			logging.error('GET returned error %s "%": %s', r.status_code, r.reason, r.text)
			r.raise_for_status()
		return r.json()


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Submit JSON files to the Event DB')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('file_paths', metavar = 'FILEPATH', nargs='+', help = 'The path to a JSON file')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	event_db = EventDB()
	
	for file_path in args.file_paths:
		
		try:
			f = open(file_path)
			event = json.load(f)
			f.close()
		except json.JSONDecodeError as why:
			logging.error('Could not parse file %s: %s', file_path, why)
			continue
		except Exception as why:
			logging.error('Could not read file %s: %s', file_path, why)
			continue
			
		logging.info('Submitting event from file %s', file_path)
		
		try:
			result = event_db.submit_event(event)
		except requests.HTTPError as why:
			logging.error('Failed to submit event: %s', why)
		except Exception as why:
			logging.critical('Failed to submit event: %s', why)
			break
		else:
			errors = event_db.get_errors(result)
			if not errors:
				logging.info('Submitted event succesfully')
				logging.debug('Result: %s', result)
			else:
				for error in errors:
					logging.error('Failed to submit event: %s', error)
