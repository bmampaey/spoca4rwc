#!/usr/bin/env python3

import sys
import argparse
import requests
import json
import logging
import importlib

# Address of the EventDB server
event_db_server = "http://solrwc1:8888/"

# Timeout in seconds for requests to the EventDB server
event_db_timeout = 100

class EventDBError(Exception):
	pass

class EventDB:
	'''Class to create, get and update events in the Event DB server'''
	
	def __init__(self, server = event_db_server, timeout = event_db_timeout):
		self.post_address = server + 'message'
		self.get_address = server + 'aquery'
		self.timeout = timeout
	
	def get_errors(self, response_data):
		'''Return the list of errors from response data'''
		if isinstance(response_data, dict) and 'error' in response_data:
			return [response_data['error']]
		elif isinstance(response_data, list):
			return [rec['error'] for rec in response_data if 'error' in rec]
		else:
			return []
	
	def post_data(self, data):
		'''POST data to the Event DB'''
		try:
			encoded_data = json.dumps(data, allow_nan = False)
		except Exception as why:
			raise EventDBError(str(why))
		
		response = requests.post(self.post_address, data = encoded_data, timeout = self.timeout, headers = {'Content-Type': 'application/json'})
		
		if response.status_code != 200:
			logging.error('POST returned error %s "%s": %s', response.status_code, response.reason, response.text)
			response.raise_for_status()
		
		response_data = response.json()
		
		errors = self.get_errors(response_data)
		if errors:
			raise EventDBError(errors)
		
		return response_data
	
	def get_data(self, params = None):
		'''GET data from the Event DB'''
		
		response = requests.get(self.get_address, params = params or {}, timeout = self.timeout)
		
		if response.status_code != 200:
			logging.error('GET returned error %s "%s": %s', response.status_code, response.reason, response.text)
			response.raise_for_status()
		
		response_data = response.json()
		
		errors = self.get_errors(response_data)
		if errors:
			raise EventDBError(errors)
		
		return response_data
	
	def get_event(self, event_type, event_name):
		'''Get an event from the Event DB'''
		params = {
			'return': event_type,
			'constraints': '{event_type}$name$eq${event_name}'.format(event_type = event_type, event_name = event_name),
		}
		
		data = self.get_data(params)
		
		return data[event_type][0]
	
	def create_event(self, event):
		'''Create a new event in the Event DB'''
		# Check if the event has already been submitted to the EventDB before
		try:
			result = self.get_event(event['event_type'], event['name'])
		except LookupError as why:
			# The event does not exists
			result = self.post_data(event)
			logging.info('Succesfully created event "%s" (%s)', event['name'], result)
		else:
			logging.warning('Trying to create previously submitted event "%s"', event['name'])
		
		return result
	
	def update_event(self, event, merge_events):
		'''Update an existing event in the Event DB'''
		# Check if the event has already been submitted to the EventDB before
		try:
			previous_event = self.get_event(event['event_type'], event['name'])
		except LookupError as why:
			# The event does not exists
			pass
		else:
			# The event needs to be updated
			logging.info('Updating event "%s"', event['name'])
			event = merge_events(event, previous_event)
			
		result = self.post_data(event)
		logging.info('Succesfully submitted event "%s" (%s)', event['name'], result)
		return result

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Create/Get/Update an event to/from the Event DB')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--get', '-g', nargs = 2, metavar = ('TYPE', 'NAME'), help = 'Get an event by type and name')
	parser.add_argument('--create', '-c', metavar = 'FILEPATH', help = 'Create an event from a JSON file')
	parser.add_argument('--update', '-u', nargs = 2, metavar = ('FILEPATH', 'METHODPATH'), help = 'Update an event from a JSON file, using merge method')
	
	args = parser.parse_args()
	
	if not(args.get or args.create or args.update):
		parser.error('No action requested, add --get or --create or --update')
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	event_db = EventDB()
	
	if args.get:
		event_type, event_name = args.get
		
		try:
			result = event_db.get_event(event_type, event_name)
		except LookupError as why:
			logging.error('Event not found')
		except EventDBError as why:
			logging.error('Failed to get event: %s', why)
		except Exception as why:
			logging.critical('Failed to get event: %s', why)
		else:
			logging.info('Got event succesfully: %s', result)
	
	elif args.create:
		file_path = args.create
		
		try:
			f = open(file_path)
			event = json.load(f)
			f.close()
		except json.JSONDecodeError as why:
			logging.critical('Could not parse file %s: %s', file_path, why)
			sys.exit(2)
		except Exception as why:
			logging.critical('Could not read file %s: %s', file_path, why)
			sys.exit(2)
		
		try:
			result = event_db.create_event(event)
		except EventDBError as why:
			logging.error('Failed to create event: %s', why)
		except Exception as why:
			logging.critical('Failed to create event: %s', why)
		else:
			logging.info('Created event succesfully: %s', result)
	
	elif args.update:
		file_path, method_path = args.update
		
		try:
			module_name, method_name = method_path.rsplit('.', 1)
			module = importlib.import_module(module_name)
			method = getattr(module, method_name)
		except Exception as why:
			logging.critical('Failed to find method "%s": %s', method_path, why)
			sys.exit(2)
		
		try:
			f = open(file_path)
			event = json.load(f)
			f.close()
		except json.JSONDecodeError as why:
			logging.critical('Could not parse file %s: %s', file_path, why)
			sys.exit(2)
		except Exception as why:
			logging.critical('Could not read file %s: %s', file_path, why)
			sys.exit(2)
		
		try:
			result = event_db.update_event(event, method)
		except EventDBError as why:
			logging.error('Failed to update event: %s', why)
		except Exception as why:
			logging.critical('Failed to update event: %s', why)
		else:
			logging.info('Updated event succesfully: %s', result)
