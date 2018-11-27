#!/usr/bin/env python3
import logging
import argparse
import json
import os
import math
from datetime import datetime
from astropy.units import pixel, km
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames

# The map HDU that contains the image
image_hdu_name = 'CoronalHoleMap'

# The map HDU that contains the regions
region_hdu_name = 'Regions'

# The map HDU that contains the chaincodes
chaincode_hdu_name = 'ChainCodes'

# The map HDUs that contains the region stats
region_stats_hdu_names = ['AIA_193_CoronalHoleStats', 'HMI_MAGNETOGRAM_CoronalHoleStats']

# The SPoCA version
spoca_version = '1'


def get_event(event_type, data, name = None):
	'''Return a container for an event'''
	event = {
		'event_type': event_type,
		'data': data,
	}
	
	if name is not None:
		event['name'] = name
	
	return event


def pixel_to_heliographic_stonyhurst(map, x, y):
	'''Convert pixel coordinates to Heliographic Stonyhurst coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	if math.isfinite(stonyhurst.lat.degree) and math.isfinite(stonyhurst.lon.degree):
		return {
			'Latitude': stonyhurst.lat.degree,
			'Longitude': stonyhurst.lon.degree,
		}
	else:
		raise ValueError('Cannot convert pixel coordinates to Heliographic Stonyhurst coordinates')


def pixel_to_heliographic_carrington(map, x, y):
	'''Convert pixel coordinates to Heliographic Carrington coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	carrington = world.transform_to(frames.HeliographicCarrington)
	
	if math.isfinite(carrington.lat.degree) and math.isfinite(carrington.lon.degree):
		return {
			'Latitude': carrington.lat.degree,
			'Longitude': carrington.lon.degree,
		}
	else:
		raise ValueError('Cannot convert pixel coordinates to Heliographic Carrington coordinates')

def pixel_to_heliocentric_earth_equatorial(map, x, y):
	'''Convert pixel coordinates to Heliocentric Earth Equatorial coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	
	# SunPy requires to use intermediate heliographic coordinates
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	heeq = stonyhurst.transform_to(frames.Heliocentric(observer="earth", obstime=map.date))
	
	if math.isfinite(heeq.x.value) and math.isfinite(heeq.y.value) and math.isfinite(heeq.z.value):
		return {
			'x': heeq.x.to(km).value,
			'y': heeq.y.to(km).value,
			'z': heeq.y.to(km).value,
		}
	else:
		raise ValueError('Cannot convert pixel coordinates to Heliocentric Earth Equatorial coordinates')


def get_heliographic_coordinate_stonyhurst(map, x, y, name = None):
	'''Return a _HeliographicCoordinate_Stonyhurst event'''
	data = pixel_to_heliographic_stonyhurst(map, x, y)
	
	return get_event('_HeliographicCoordinate_Stonyhurst', data, name = name)


def get_heliographic_coordinate_carrington(map, x, y, name = None):
	'''Return a _HeliographicCoordinate_Carrington event'''
	data = pixel_to_heliographic_carrington(map, x, y)
	
	return get_event('_HeliographicCoordinate_Carrington', data, name = name)


def get_heliocentric_coordinate_heeq(map, x, y, name = None):
	'''Return a _HeliocentricCoordinate_HEEQ event'''
	data = pixel_to_heliocentric_earth_equatorial(map, x, y)
	
	return get_event('_HeliocentricCoordinate_HEEQ', data, name = name)


def get_heliographic_coordinate(map, x, y, time, name = None):
	'''Return a _HeliographicCoordinate event'''
	data = {
		'Time': time,
		'Stonyhurst': get_heliographic_coordinate_stonyhurst(map, x, y),
		'Carrington': get_heliographic_coordinate_carrington(map, x, y),
	}
	
	return get_event('_HeliographicCoordinate', data, name = name)


def get_solar_surface_contour(map, x, y, name = None):
	'''Return a _SolarSurface_Contour event'''
	data = {
		'Stonyhurst': get_heliographic_coordinate_stonyhurst(map, x, y),
		'Carrington': get_heliographic_coordinate_carrington(map, x, y),
		'HEEQ': get_heliocentric_coordinate_heeq(map, x, y),
	}
	
	return get_event('_SolarSurface_Contour', data, name = name)


def get_spoca_coronal_hole(spoca_coronal_hole_detection_name, time, name = None):
	'''Return a SPOCA_CoronalHole event'''
	data = {
		'Detections': [spoca_coronal_hole_detection_name],
		'BeginTime': time,
		'EndTime': time,
		#'Polarity': None,
	}
	
	return get_event('SPOCA_CoronalHole', data, name = name)


def get_spoca_coronal_hole_detection(map, region, region_stat, chaincode, name = None):
	'''Return a SPOCA_CoronalHoleDetection event'''
	
	# Compute the chain code
	contour = list()
	for x, y in zip(*chaincode):
		# If x and y are both 0 then it is the end of the chaincode
		if (x == 0 and y == 0):
			break
		else:
			# If we cannot convert some pixel coordinates to sun coordinates, we just skip it
			try:
				contour.append(get_solar_surface_contour(map, x, y))
			except ValueError:
				pass
	
	data = {
		'DetectionTime': region['DATE_OBS'] + 'Z',
		'AreaError': float(region_stat['AREA_ATDISKCENTER_UNCERTAINITY']),
		'Area': float(region_stat['AREA_ATDISKCENTER']),
		'Location': get_heliographic_coordinate(map, region_stat['XCENTER'], region_stat['YCENTER'], region['DATE_OBS'] + 'Z'),
		'Contour': contour,
	}
	
	return get_event('SPOCA_CoronalHoleDetection', data, name = name)


def get_spoca_coronal_hole_detection_statistics(detection, channel, region_stat, name = None):
	'''Return a SPOCA_CoronalHoleDetectionStatistics event'''
	data = {
		'Detection': detection,
		'ImageChannel': channel,
		'ImageTime': region_stat['DATE_OBS'] + 'Z',
		'Min': float(region_stat['MIN_INTENSITY']),
		'Max': float(region_stat['MAX_INTENSITY']),
		'Median': float(region_stat['MEDIAN_INTENSITY']),
		'FirstQuartile': float(region_stat['LOWERQUARTILE_INTENSITY']),
		'ThirdQuartile': float(region_stat['UPPERQUARTILE_INTENSITY']),
		'Mean': float(region_stat['MEAN_INTENSITY']),
		'Var': float(region_stat['VARIANCE']),
		'Skewness': float(region_stat['SKEWNESS']),
		'Kurtosis': float(region_stat['KURTOSIS']),
		'PixelsNumber': int(region_stat['NUMBER_GOOD_PIXELS']),
	}
	
	return get_event('SPOCA_CoronalHoleDetectionStatistics', data, name = name)


def get_spoca_coronal_hole_run(image_time, detections, run_time = None, version = spoca_version, name = None):
	'''Return a SPOCA_CoronalHoleRun event'''
	
	data = {
		'RunTime': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') if run_time is None else run_time,
		'ImageTime': image_time,
		'VersionNb': version,
		'Detections': detections,
	}
	
	return get_event('SPOCA_CoronalHoleRun', data, name = name)


def get_CHMap_events(map_path):
	'''Return all the SPOCA_CoronalHole, SPOCA_CoronalHoleDetection and SPOCA_CoronalHoleDetectionStatistics events in a SPoCA CHMap'''
	# Open the FITS file
	hdus = fits.open(map_path)
	
	# Create a sunpy Map for converting the pixel coordinates
	image_hdu = hdus[image_hdu_name]
	map = Map(image_hdu.data, image_hdu.header)
	
	# Get the regions by id
	regions_hdu = hdus[region_hdu_name]
	regions = {
		region['ID']: region
		for region in regions_hdu.data
	}
	
	# Get chaincodes by id
	chaincodes_hdu = hdus[chaincode_hdu_name]
	chaincodes = {
		id: (chaincodes_hdu.data['X%07d' % id], chaincodes_hdu.data['Y%07d' % id])
		for id in regions_hdu.data['ID']
	}
	
	# Get region stats by channel then by id
	region_stats = {
		hdus[region_stats_hdu_name].header['CHANNEL']: {
			region_stat['ID']: region_stat
			for region_stat in hdus[region_stats_hdu_name].data
		}
		for region_stats_hdu_name in region_stats_hdu_names if region_stats_hdu_name in hdus
	}
	
	
	# Create the CH events
	CH_events = dict()
	
	# Keep the list of detections for the SPOCA_CoronalHoleRun event
	detection_names = list()
	
	for id, region in regions.items():
		
		events = dict()
		
		spoca_coronal_hole_detection_name = 'SPOCA_CoronalHoleDetection_{date}_{id}'.format(date=region['DATE_OBS'], id=id)
		events['spoca_coronal_hole_detection'] = get_spoca_coronal_hole_detection(map, region, next(iter(region_stats.values()))[id], chaincodes[id], name = spoca_coronal_hole_detection_name)
		
		spoca_coronal_hole_name = 'SPOCA_CoronalHole_{color}'.format(color=region['TRACKED_COLOR'])
		events['spoca_coronal_hole'] = get_spoca_coronal_hole(spoca_coronal_hole_detection_name, region['DATE_OBS'] + 'Z', name = spoca_coronal_hole_name)
		
		events['spoca_coronal_hole_detection_statistics'] = list()
		for channel, stats in region_stats.items():
			spoca_coronal_hole_detection_statistics_name = 'SPOCA_CoronalHoleDetectionStatistics_{date}_{id}_{channel}'.format(date=region['DATE_OBS'], id=id, channel=channel)
			events['spoca_coronal_hole_detection_statistics'].append(get_spoca_coronal_hole_detection_statistics(spoca_coronal_hole_detection_name, channel, stats[id], name = spoca_coronal_hole_detection_statistics_name))
		
		CH_events[spoca_coronal_hole_name] = events
		
		detection_names.append(spoca_coronal_hole_detection_name)
	
	# Create the run event
	image_date = image_hdu.header['DATE_OBS'].split('.')[0] # We don't want the subsecond
	spoca_coronal_hole_run_name = 'SPOCA_CoronalHoleRun_{date}'.format(date=image_date)
	run_event = get_spoca_coronal_hole_run(image_date + 'Z', detection_names, name = spoca_coronal_hole_run_name)
	
	return run_event, CH_events


def merge_spoca_coronal_hole(spoca_coronal_hole1, spoca_coronal_hole2):
	'''Update a SPOCA_CoronalHole event with another SPOCA_CoronalHole event'''
	if spoca_coronal_hole2:
		spoca_coronal_hole1['data']['Detections'].extend(spoca_coronal_hole2['data']['Detections'])
		spoca_coronal_hole1['data']['BeginTime'] = min(spoca_coronal_hole1['data']['BeginTime'], spoca_coronal_hole2['data']['BeginTime'])
		spoca_coronal_hole1['data']['EndTime'] = max(spoca_coronal_hole1['data']['EndTime'], spoca_coronal_hole2['data']['EndTime'])
	
	return spoca_coronal_hole1


def write_events(*events, output_directory = '.'):
	'''Write all the events to JSON files'''
	for event in events:
		file_path = os.path.join(output_directory, event['name'] + '.json')
		logging.info('Writing JSON file %s', file_path)
		with open(file_path, 'w') as f:
			json.dump(event, f, ensure_ascii = False, indent = '\t')


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CHMap and write corresponding events to JSON files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', help = 'The file path of the log file')
	parser.add_argument('--output_directory', '-o', default = '.', help = 'The output directory for the JSON files')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The path to a SPoCA CHMap')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.log_file:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	# Dict of all known SPOCA_CoronalHole events per name
	spoca_coronal_holes = dict()
	
	for map_path in args.maps:
		logging.info('Parsing map %s', map_path)
		
		# Get all events in the CHMap
		run_event, CH_events = get_CHMap_events(map_path)
		
		# Write the CH events
		for name, events in CH_events.items():
			
			# Update the SPOCA_CoronalHole event with known coronal holes
			spoca_coronal_holes[name] = merge_spoca_coronal_hole(events['spoca_coronal_hole'], spoca_coronal_holes.get(name))
			
			# Write the events to JSON
			write_events(events['spoca_coronal_hole'], events['spoca_coronal_hole_detection'], *events['spoca_coronal_hole_detection_statistics'], output_directory = args.output_directory)
		
		# Write the run event
		write_events(run_event, output_directory = args.output_directory)
