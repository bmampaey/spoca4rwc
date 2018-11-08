#!/usr/bin/env python3
import logging
import argparse
import json
import os
from astropy.units import pixel
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
region_stats_hdu_names = ['AIA_193_CoronalHoleStats']


def get_event(event_type, data, name = None):
	'''Return a container for an event'''
	event = {
		'event_type': event_type,
		'data': data,
	}
	
	if name is not None:
		event['name'] = name
	
	return event


def to_heliographic_coordinate_stonyhurst(map, x, y):
	'''Convert pixel coordinates to Stonyhurst coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	return {
		'Latitude': stonyhurst.lat.degree,
		'Longitude': stonyhurst.lon.degree,
	}


def to_heliographic_coordinate_carrington(map, x, y):
	'''Convert pixel coordinates to Carrington coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	carrington = world.transform_to(frames.HeliographicCarrington)
	
	return {
		'Latitude': carrington.lat.degree,
		'Longitude': carrington.lon.degree,
	}


def get_heliographic_coordinate_stonyhurst(map, x, y, name = None):
	'''Return a _HeliographicCoordinate_Stonyhurst event'''
	data = to_heliographic_coordinate_stonyhurst(map, x, y)
	
	return get_event('_HeliographicCoordinate_Stonyhurst', data, name = name)


def get_heliographic_coordinate_carrington(map, x, y, name = None):
	'''Return a _HeliographicCoordinate_Carrington event'''
	data = to_heliographic_coordinate_carrington(map, x, y)
	
	return get_event('_HeliographicCoordinate_Carrington', data, name = name)


def get_heliographic_coordinate(map, x, y, time, name = None):
	'''Return a _HeliographicCoordinate event'''
	data = {
		'Time': time,
		'Stonyhurst': get_heliographic_coordinate_stonyhurst(map, x, y),
		'Carrington': get_heliographic_coordinate_carrington(map, x, y),
	}
	
	return get_event('_HeliographicCoordinate', data, name = name)


def get_solar_surface_bounding_box(map, sw_x, sw_y, ne_x, ne_y, name = None):
	'''Return a _SolarSurface_BoundingBox event'''
	data = {
		'StonyhurstSW': get_heliographic_coordinate_stonyhurst(map, sw_x, sw_y),
		'StonyhurstNE': get_heliographic_coordinate_stonyhurst(map, ne_x, ne_y),
		'CarringtonSW': get_heliographic_coordinate_carrington(map, sw_x, sw_y),
		'CarringtonNE': get_heliographic_coordinate_carrington(map, ne_x, ne_y),
	}
	
	return get_event('_SolarSurface_BoundingBox', data, name = name)


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
	data = {
		'DetectionTime': region['DATE_OBS'] + 'Z',
		'AreaError': float(region_stat['AREA_ATDISKCENTER_UNCERTAINITY']),
		'Area': float(region_stat['AREA_ATDISKCENTER']),
		'Location': get_heliographic_coordinate(map, region_stat['XCENTER'], region_stat['YCENTER'], region['DATE_OBS'] + 'Z'),
		'BoundingBox': get_solar_surface_bounding_box(map, region['XBOXMIN'], region['YBOXMIN'], region['XBOXMAX'], region['YBOXMAX']),
		'Contour': [get_heliographic_coordinate_stonyhurst(map, x, y) for x, y in zip(*chaincode) if (x != 0 or y != 0)],
	}
	
	return get_event('SPOCA_CoronalHoleDetection', data, name = name)


def get_spoca_coronal_hole_detection_statistics(detection, channel, region_stat, name = None):
	'''Return a SPOCA_CoronalHoleDetectionStatistics event'''
	data = {
		'Detection': detection,
		'ImageChannel': channel,
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
		for region_stats_hdu_name in region_stats_hdu_names
	}
	
	# Create the events
	events = dict()
	
	for id, region in regions.items():
		
		new_events = dict()
		
		spoca_coronal_hole_detection_name = 'SPOCA_CoronalHoleDetection_{date}_{id}'.format(date=region['DATE_OBS'], id=id)
		new_events['spoca_coronal_hole_detection'] = get_spoca_coronal_hole_detection(map, region, next(iter(region_stats.values()))[id], chaincodes[id], name = spoca_coronal_hole_detection_name)
		
		spoca_coronal_hole_name = 'SPOCA_CoronalHole_{color}'.format(color=region['TRACKED_COLOR'])
		new_events['spoca_coronal_hole'] = get_spoca_coronal_hole(spoca_coronal_hole_detection_name, region['DATE_OBS'] + 'Z', name = spoca_coronal_hole_name)
		
		new_events['spoca_coronal_hole_detection_statistics'] = list()
		for channel, stats in region_stats.items():
			spoca_coronal_hole_detection_statistics_name = 'SPOCA_CoronalHoleDetectionStatistics_{date}_{id}_{channel}'.format(date=region['DATE_OBS'], id=id, channel=channel)
			new_events['spoca_coronal_hole_detection_statistics'].append(get_spoca_coronal_hole_detection_statistics(spoca_coronal_hole_detection_name, channel, stats[id], name = spoca_coronal_hole_detection_statistics_name))
		
		events[spoca_coronal_hole_name] = new_events
	
	return events


def update_spoca_coronal_hole(spoca_coronal_hole1, spoca_coronal_hole2):
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
		map_events = get_CHMap_events(map_path)
		
		for name, events in map_events.items():
			
			# Update the SPOCA_CoronalHole event with known coronal holes
			spoca_coronal_holes[name] = update_spoca_coronal_hole(events['spoca_coronal_hole'], spoca_coronal_holes.get(name))
			
			# Write the events to JSON
			write_events(events['spoca_coronal_hole'], events['spoca_coronal_hole_detection'], *events['spoca_coronal_hole_detection_statistics'], output_directory = args.output_directory)
