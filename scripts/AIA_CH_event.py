#!/usr/bin/env python3
import logging
import argparse
import json
import os
from astropy.units import pixel
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames


# Default path for the log file
log_file =  '/home/rwceventdb/log/AIA_CH_get_event.log'

# The map HDU that contains the image
image_hdu_name = 'CoronalHoleMap'

# The map HDU that contains the regions
region_hdu_name = 'Regions'

# The map HDU that contains the chaincodes
chaincode_hdu_name = 'ChainCodes'

# The map HDU that contains the region stats
region_stats_hdu_name = 'AIA_193_CoronalHoleStats'

def get_event(event_type, data, name = None):
	event = {
		'event_type': event_type,
		'data': data,
	}
	
	if name is not None:
		event['name'] = name
	
	return event

def get_heliographic_coordinate_stonyhurst(map, x, y):
	'''Convert pixel coordinates to Stonyhurst coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	return {
		'Latitude': stonyhurst.lat.degree,
		'Longitude': stonyhurst.lon.degree,
	}

def get_heliographic_coordinate_carrington(map, x, y):
	'''Convert pixel coordinates to Carrington coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	carrington = world.transform_to(frames.HeliographicCarrington)
	
	return {
		'Latitude': carrington.lat.degree,
		'Longitude': carrington.lon.degree,
	}
	
	return heliographic_coordinate_carrington

def get_heliographic_coordinate(map, x, y, time):
	stonyhurst = get_heliographic_coordinate_stonyhurst(map, x, y)
	
	carrington = get_heliographic_coordinate_carrington(map, x, y)
	
	return {
		'Time': time,
		'Stonyhurst': get_event('_HeliographicCoordinate_Stonyhurst', stonyhurst),
		'Carrington': get_event('_HeliographicCoordinate_Carrington', carrington),
	}

def get_solar_surface_bounding_box(map, sw_x, sw_y, ne_x, ne_y):
	stonyhurst_sw = get_heliographic_coordinate_stonyhurst(map, sw_x, sw_y)
	
	stonyhurst_ne = get_heliographic_coordinate_stonyhurst(map, ne_x, ne_y)
	
	carrington_sw = get_heliographic_coordinate_carrington(map, sw_x, sw_y)
	
	carrington_ne = get_heliographic_coordinate_carrington(map, ne_x, ne_y)
	
	return {
		'StonyhurstSW': get_event('_HeliographicCoordinate_Stonyhurst', stonyhurst_sw),
		'StonyhurstNE': get_event('_HeliographicCoordinate_Stonyhurst', stonyhurst_ne),
		'CarringtonSW': get_event('_HeliographicCoordinate_Carrington', carrington_sw),
		'CarringtonNE': get_event('_HeliographicCoordinate_Carrington', carrington_ne),
	}

def get_spoca_coronal_hole(spoca_coronal_hole_detection_name, time):
	return {
		'Detections': [spoca_coronal_hole_detection_name],
		'BeginTime': time,
		'EndTime': time,
		#'Polarity': None,
	}

def update_spoca_coronal_hole(spoca_coronal_hole, spoca_coronal_hole_detection_name, time):
	spoca_coronal_hole['Detections'].append(spoca_coronal_hole_detection_name)
	spoca_coronal_hole['BeginTime'] = min(spoca_coronal_hole['BeginTime'], time)
	spoca_coronal_hole['EndTime'] = max(spoca_coronal_hole['EndTime'], time)
	return spoca_coronal_hole

def get_spoca_coronal_hole_detection(map, region, region_stat, chaincode):
	
	location = get_heliographic_coordinate(map, region_stat['XCENTER'], region_stat['YCENTER'], region['DATE_OBS'] + 'Z')
	
	bounding_box = get_solar_surface_bounding_box(map, region['XBOXMIN'], region['YBOXMIN'], region['XBOXMAX'], region['YBOXMAX'])
	
	contour = (get_heliographic_coordinate_stonyhurst(map, x, y) for x, y in zip(*chaincode) if (x != 0 or y != 0))
	
	return {
		'AreaError': float(region_stat['AREA_ATDISKCENTER_UNCERTAINITY']),
		'Area': float(region_stat['AREA_ATDISKCENTER']),
		'Location': get_event('_HeliographicCoordinate', location),
		'BoundingBox': get_event('_SolarSurface_BoundingBox', bounding_box),
		'DetectionTime': region['DATE_OBS'] + 'Z',
		'Contour': [get_event('_HeliographicCoordinate_Stonyhurst', c) for c in contour],
	}

def get_spoca_coronal_hole_detection_statistics(detection, channel, region_stat):
	return {
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


def write_json(file_path, obj):
	logging.info('Writing JSON file %s', file_path)
	with open(file_path, 'w') as f:
		json.dump(obj, f, ensure_ascii = False, indent = '\t')

def parse_CH_map(map_path, output_directory = '.'):
	# Read the FITS file HDUs
	hdus = fits.open(map_path)
	image_hdu = hdus[image_hdu_name]
	regions_hdu = hdus[region_hdu_name]
	chaincodes_hdu = hdus[chaincode_hdu_name]
	region_stats_hdu = hdus[region_stats_hdu_name]
	
	# Create a sunpy Map for converting the pixel coordinates
	map = Map(image_hdu.data, image_hdu.header)
	
	# Get the data of the regions by id
	regions = {region['ID']: region for region in regions_hdu.data}
	region_stats = {region_stat['ID']: region_stat for region_stat in region_stats_hdu.data}
	chaincodes = {id: (chaincodes_hdu.data['X%07d' % id], chaincodes_hdu.data['Y%07d' % id]) for id in regions_hdu.data['ID']}
	
	for id, region in regions.items():
		spoca_coronal_hole_name = 'SPOCA_CoronalHole_{color}'.format(color=region['TRACKED_COLOR'])
		spoca_coronal_hole_detection_name = 'SPOCA_CoronalHoleDetection_{date}_{id}'.format(id=id, date=region['DATE_OBS'])
		
		spoca_coronal_hole = get_spoca_coronal_hole(spoca_coronal_hole_detection_name, region['DATE_OBS'] + 'Z')
		spoca_coronal_hole_event = get_event('SPOCA_CoronalHole', spoca_coronal_hole, name = spoca_coronal_hole_name)
		write_json(os.path.join(output_directory, spoca_coronal_hole_name + '.json'), spoca_coronal_hole_event)
		
		spoca_coronal_hole_detection = get_spoca_coronal_hole_detection(map, region, region_stats[id], chaincodes[id])
		spoca_coronal_hole_detection_event = get_event('SPOCA_CoronalHoleDetection', spoca_coronal_hole_detection, name = spoca_coronal_hole_detection_name)
		write_json(os.path.join(output_directory, spoca_coronal_hole_detection_name + '.json'), spoca_coronal_hole_detection_event)
		
		channel = region_stats_hdu.header['CHANNEL']
		spoca_coronal_hole_detection_statistics_name = 'SPOCA_CoronalHoleDetectionStatistics_{date}_{id}_{channel}'.format(id=id, date=region['DATE_OBS'], channel=channel)
		spoca_coronal_hole_detection_statistics = get_spoca_coronal_hole_detection_statistics(spoca_coronal_hole_detection_name, channel, region_stats[id])
		spoca_coronal_hole_detection_statistics_event = get_event('SPOCA_CoronalHoleDetectionStatistics', spoca_coronal_hole_detection_statistics, spoca_coronal_hole_detection_statistics_name)
		write_json(os.path.join(output_directory, spoca_coronal_hole_detection_statistics_name + '.json'), spoca_coronal_hole_detection_statistics_event)



# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CH map and write corresponding events to JSON files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', default = log_file, help = 'The file path of the log file')
	parser.add_argument('--output_directory', '-o', default = '.', help = 'The output directory for the JSON files')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The path to a SPoCA CH map')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.debug:
		logging.basicConfig(level = logging.DEBUG, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	
	for map_path in args.maps:
		logging.info('Parsing map %s', map_path)
		parse_CH_map(map_path, output_directory = args.output_directory)
		
