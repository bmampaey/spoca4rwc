#!/usr/bin/env python3

import argparse
import requests
import json
import logging

# Address of the EventDB server
eventdb_server = "http://solrwc2:8888/"

# Timeout in seconds for requests to the EventDB server
eventdb_timeout = 10

class EventDBError(Exception):
	pass

class EventDB:
	'''Class to manage POST and GET to the Event DB server'''
	
	def __init__(self, server = eventdb_server, timeout = eventdb_timeout):
		self.submit_address = server + 'message'
		self.get_address = server + 'aquery'
		self.timeout = timeout
	
	def get_errors(self, response):
		if isinstance(response, dict) and 'error' in response:
			return [response['error']]
		elif isinstance(response, list):
			return [rec['error'] for rec in response if 'error' in rec]
		else:
			return []
	
	def submit_event(self, event = eventdb_server):
		
		try:
			data = json.dumps(event, allow_nan = False)
		except Exception as why:
			raise EventDBError(str(why))
		
		response = requests.post(self.submit_address, data = data, timeout = self.timeout, headers = {'Content-Type': 'application/json'})
		
		if response.status_code != 200:
			logging.error('POST returned error %s "%s": %s', response.status_code, response.reason, response.text)
			response.raise_for_status()
		
		data = response.json()
		
		errors = self.get_errors(data)
		if errors:
			raise EventDBError(errors)
		
		return data
	
	def get_event(self, event_type, event_name):
		params = {
			'return': event_type,
			'constraints': '{event_type}$name$eq${event_name}'.format(event_type = event_type, event_name = event_name),
		}
		
		response = requests.get(self.get_address, params = params, timeout = self.timeout)
		if response.status_code != 200:
			logging.error('GET returned error %s "%": %s', response.status_code, response.reason, response.text)
			response.raise_for_status()
		
		data = response.json()
		
		errors = self.get_errors(data)
		if errors:
			raise EventDBError(errors)
		
		return data[event_type][0]


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Submit JSON files to the Event DB')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--submit', '-s', metavar = 'FILEPATH', help = 'Submit an event from a JSON file')
	parser.add_argument('--get', '-g', nargs = 2, metavar = ('TYPE', 'NAME'), help = 'Get an event by type and name')
	
	args = parser.parse_args()
	
	if not(args.submit or args.get):
		parser.error('No action requested, add --submit or --get')
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	eventdb = EventDB()
	
	if args.submit:
		file_path = args.submit
		
		try:
			f = open(file_path)
			event = json.load(f, allow_nan=False)
			f.close()
		except json.JSONDecodeError as why:
			logging.error('Could not parse file %s: %s', file_path, why)
		except Exception as why:
			logging.error('Could not read file %s: %s', file_path, why)
		
		try:
			result = eventdb.submit_event(event)
		except EventDBError as why:
			logging.error('Failed to submit event: %s', why)
		except Exception as why:
			logging.critical('Failed to submit event: %s', why)
		else:
			logging.info('Submitted event succesfully: %s', result)
	
	if args.get:
		event_type, event_name = args.get
		try:
			result = eventdb.get_event(event_type, event_name)
		except LookupError as why:
			logging.error('Event not found')
		except EventDBError as why:
			logging.error('Failed to get event: %s', why)
		except Exception as why:
			logging.critical('Failed to get event: %s', why)
		else:
			logging.info('Got event succesfully: %s', result)
