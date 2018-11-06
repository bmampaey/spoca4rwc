#!/usr/bin/env python3
import logging
import argparse
from astropy.units import pixel
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames

from CH_schema import _HeliographicCoordinate, _HeliographicCoordinate_Stonyhurst, _HeliographicCoordinate_Carrington, _SolarSurface_BoundingBox, SPOCA_CoronalHole, SPOCA_CoronalHoleDetection, SPOCA_CoronalHoleDetectionStatistics
from CH_schema import FT__HeliographicCoordinate, FT__HeliographicCoordinate_Stonyhurst, FT__HeliographicCoordinate_Carrington, FT__SolarSurface_BoundingBox, FT_SPOCA_CoronalHole, FT_SPOCA_CoronalHoleDetection, FT_SPOCA_CoronalHoleDetectionStatistics

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

def get_FT(cls, data, name = None, event_type = None):
	params = {
	'data': data
	}
	
	if name is not None:
		params['name'] = name
	
	if event_type is not None:
		params['event_type'] = event_type
	
	return cls(**params)

def get_heliographic_coordinate_stonyhurst(map, x, y):
	'''Convert pixel coordinates to Stonyhurst coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	heliographic_coordinate_stonyhurst = _HeliographicCoordinate_Stonyhurst(
		Latitude = stonyhurst.lat.degree,
		Longitude = stonyhurst.lon.degree,
	)
	
	return heliographic_coordinate_stonyhurst

def get_heliographic_coordinate_carrington(map, x, y):
	'''Convert pixel coordinates to Carrington coordinates'''
	world = map.pixel_to_world(x * pixel, y * pixel, origin = 1)
	carrington = world.transform_to(frames.HeliographicCarrington)
	
	heliographic_coordinate_carrington = _HeliographicCoordinate_Carrington(
		Latitude = carrington.lat.degree,
		Longitude = carrington.lon.degree,
	)
	
	return heliographic_coordinate_carrington

def get_heliographic_coordinate(map, x, y, time):
	heliographic_coordinate = _HeliographicCoordinate(
		Carrington = get_heliographic_coordinate_carrington(map, x, y),
		Stonyhurst = get_heliographic_coordinate_stonyhurst(map, x, y),
		Time = time
	)
	return heliographic_coordinate

def get_solar_surface_bounding_box(map, sw_x, sw_y, ne_x, ne_y):
	solar_surface_bounding_box = _SolarSurface_BoundingBox(
		StonyhurstNE = get_heliographic_coordinate_stonyhurst(map, ne_x, ne_y),
		CarringtonNE = get_heliographic_coordinate_carrington(map, ne_x, ne_y),
		CarringtonSW = get_heliographic_coordinate_carrington(map, sw_x, sw_y),
		StonyhurstSW = get_heliographic_coordinate_stonyhurst(map, sw_x, sw_y),
	)
	return solar_surface_bounding_box

def get_spoca_coronal_hole(spoca_coronal_hole_detection):
	spoca_coronal_hole = SPOCA_CoronalHole(
		Polarity = None,
		Detections = [spoca_coronal_hole_detection],
		EndTime = spoca_coronal_hole_detection.DetectionTime,
		BeginTime = spoca_coronal_hole_detection.DetectionTime,
	)
	return spoca_coronal_hole

def get_spoca_coronal_hole_detection(map, region, region_stat, chaincode):
	
	location = get_heliographic_coordinate(map, region_stat['XCENTER'], region_stat['YCENTER'], region['DATE_OBS'])
	
	bounding_box = get_solar_surface_bounding_box(map, region['XBOXMIN'], region['YBOXMIN'], region['XBOXMAX'], region['YBOXMAX'])
	
	contour = [get_heliographic_coordinate_stonyhurst(map, x, y) for x, y in zip(*chaincode) if x != 0 and y != 0]
	
	spoca_coronal_hole_detection = SPOCA_CoronalHoleDetection(
		Statistics = [],
		AreaError = float(region_stat['AREA_ATDISKCENTER_UNCERTAINITY']),
		Area = float(region_stat['AREA_ATDISKCENTER']),
		Location = location,
		BoundingBox = bounding_box,
		DetectionTime = region['DATE_OBS'],
		Contour = contour,
	)
	
	return spoca_coronal_hole_detection

def get_spoca_coronal_hole_detection_statistics(channel, region_stat):
	spoca_coronal_hole_detection_statistics = SPOCA_CoronalHoleDetectionStatistics(
		Detection = [],
		ImageChannel = channel,
		#DetectionTime = region_stat['DATE_OBS'],
		Min = float(region_stat['MIN_INTENSITY']),
		Max = float(region_stat['MAX_INTENSITY']),
		Median = float(region_stat['MEDIAN_INTENSITY']),
		FirstQuartile = float(region_stat['LOWERQUARTILE_INTENSITY']),
		ThirdQuartile = float(region_stat['UPPERQUARTILE_INTENSITY']),
		Mean = float(region_stat['MEAN_INTENSITY']),
		Var = float(region_stat['VARIANCE']),
		Skewness = float(region_stat['SKEWNESS']),
		Kurtosis = float(region_stat['KURTOSIS']),
		PixelsNumber = float(region_stat['NUMBER_GOOD_PIXELS']),
	)
	
	return spoca_coronal_hole_detection_statistics

def parse_CH_map(map_path):
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
		import ipdb; ipdb.set_trace()
		spoca_coronal_hole_detection_statistics = get_spoca_coronal_hole_detection_statistics(region_stats_hdu.header['CHANNEL'], region_stats[id])
		spoca_coronal_hole_detection = get_spoca_coronal_hole_detection(map, region, region_stats[id], chaincodes[id])
		spoca_coronal_hole = get_spoca_coronal_hole(spoca_coronal_hole_detection)
		

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CH map and create corresponding events')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', default = log_file, help = 'The file path of the log file')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The path to a SPoCA CH map')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.debug:
		logging.basicConfig(level = logging.DEBUG, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	
	for map_path in args.maps:
		parse_CH_map(map_path)
		
