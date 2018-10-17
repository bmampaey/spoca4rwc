#!/usr/bin/env python3
import os
import configparser
import subprocess
import argparse


class Job:
	'''Base class to run a program'''
	def __init__(self, executable, *args, **kwargs):
		self.executable = executable
		self.args = args
		self.kwargs = kwargs
	
	def get_command(self, args = None, kwargs = None):
		'''Return the command with the parameters set up'''
		
		# Merge init args and passed args
		if args:
			merged_args = self.args + args
		else:
			merged_args = self.args
		
		# Merge init kwargs and passed kwargs
		if kwargs:
			# Passed kwargs take precedence over init kwargs
			merged_kwargs = self.kwargs.copy()
			merged_kwargs.update(kwargs)
		else:
			merged_kwargs = self.kwargs
		
		# Add executable
		command = [self.executable]
		
		# Add kwargs
		for key, value in merged_kwargs.items():
			command.append('--'+key)
			if value:
				command.append(value)
		
		# Add args
		command.extend(merged_args)
		
		return command
	
	def __call__(self, *args, input = None, **kwargs):
		'''Run the program'''
		
		command = self.get_command(args, kwargs)
		
		process = subprocess.run(command, input = input, stdout = subprocess.PIPE, stderr = subprocess.PIPE, encoding = 'utf8')
		
		return process.returncode, process.stdout, process.stderr
	
	def __str__(self):
		return ' '.join(self.get_command())


# Start point of the script
if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description = 'Run a SPoCA program', prefix_chars = '-')
	parser.add_argument('executable', help = 'The path to the executable')
	parser.add_argument('parameters', metavar = 'PARAM', nargs = '*', help = 'Any additional parameter (must be preceded by "--")')
	
	args = parser.parse_args()
	
	program = Job(args.executable, *args.parameters)
	
	print(program)
	
	result = program()
	
	print('Return:%s\nOutput:%s\nError:%s' % result)
	
