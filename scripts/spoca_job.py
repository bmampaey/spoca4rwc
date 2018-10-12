#!/usr/bin/env python3
import os
import configparser
import subprocess
import argparse


class Job:
	'''Base class to run a program'''
	def __init__(self, bin, config_file = None, args = [], kwargs = {}):
		self.bin = bin
		self.args = list()
		self.kwargs = dict()
		
		if config_file is not None:
			config = self.parse_config_file(config_file)
			self.kwargs.update(config.defaults())
		
		self.args.extend(args)
		self.kwargs.update(kwargs)
	
	def parse_config_file(self, config_file):
		'''Parse a config file and return it as a config object'''
		config = configparser.ConfigParser()
		
		try:
			config.read(config_file)
		except configparser.MissingSectionHeaderError as why:
			# If no section is defined, add a default one
			with open(config_file) as f:
				text = f.read()
			config.read_string('[DEFAULT]\n' + text, source=config_file)
		
		return config
	
	def get_parameters(self, args = [], kwargs = {}):
		'''Return the parameters for the program'''
		# Merge init kwargs and passed kwargs
		merged_kwargs = self.kwargs.copy()
		merged_kwargs.update(kwargs)
		
		parameters = list()
		for key, value in merged_kwargs.items():
			if len(key) > 1:
				parameters.append('--'+key)
			else:
				parameters.append('-'+key)
			if value:
				parameters.append(value)
		
		# Add init args and passed args
		parameters.extend(self.args + args)
		
		return parameters
	
	def __call__(self, input = None, args = [], kwargs = {}):
		'''Run the program'''
		command = [self.bin] + self.get_parameters(args, kwargs)
		
		process = subprocess.run(command, input = input, stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding='utf8')
		
		return process.returncode, process.stdout, process.stderr
	
	def __str__(self):
		return ' '.join([self.bin] + self.get_parameters())


class Classification(Job):
	'''Job to run the classification program'''
	MAP_TYPES = {
		'A': 'ARMap',
		'C': 'CHMap',
		'S': 'SegmentedMap',
		'M': 'MixedMap'
	}
	
	def test_parameters(self):
		'''Test the parameters of the program'''
		if not os.path.exists(self.bin):
			return False, 'Could not find executable "%s"' % self.bin
		
		return_code, output, error = self(args = ['--help', 'testfile.fits'])
		
		return return_code == 0, 'Output: %s\nError: %s' % (output, error)
	
	def result_files(self, name):
		'''Return the file names of the result files from the classification'''
		results = list()
		for m, suffix in cls.MAP_TYPES.items():
			if self.kwargs['maps'].find(m) > -1:
				results.append('.'.join([name, suffix, 'fits']))
		return results


class Tracking(Job):
	'''Job to run the tracking program'''
	
	def test_parameters(self):
		'''Test the parameters of the program'''
		if not os.path.exists(self.bin):
			return False, 'Could not find executable "%s"' % self.bin
		
		return_code, output, error = self(args = ['--help', 'testfile1.fits', 'testfile2.fits'])
		
		return return_code == 0, 'Output: %s\nError: %s' % (output, error)


# Start point of the script
if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='Test the parameters of a SPoCA program')
	parser.add_argument('program', help='The program to test')
	parser.add_argument('executable', help='The path to the executable')
	parser.add_argument('config', help='The path to the config file')
	parser.add_argument('parameter', nargs='*', help='Any additional parameter (must be preceded by -- delimiter)')
	
	args = parser.parse_args()
	
	if args.program.lower() == 'classification':
		job = Classification(args.executable, args.config, args.parameter)
	elif args.program.lower() == 'tracking':
		job = Tracking(args.executable, args.config, args.parameter)
	else:
		job = None
	
	if job is None:
		print('Unknown program')
	else:
		print(job)
		result, output = job.test_parameters()
		if result:
			print('--- PARAMETERS SEEM GOOD ---')
		else:
			print('--- PARAMETERS SEEM BAD ---')
		print(output)
