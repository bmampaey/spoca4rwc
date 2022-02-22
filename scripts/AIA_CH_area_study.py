#!/usr/bin/env python3
import logging
import argparse
import csv
from astropy.units import pixel, km
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames

# The map HDU that contains the image
image_hdu_name = 'CoronalHoleMap'

# The map HDU that contains the regions
region_hdu_name = 'Regions'

# The map HDUs that contains the region stats
region_stats_hdu_name = 'AIA_193_CoronalHoleStats'

def get_heliographic_coordinate_stonyhurst(map, x, y, origin = 0):
	'''Convert pixel coordintaes to Heliographic Stonyhurst Longitude Latitude'''
	
	# The FITS coordinate system starts at (1, 1) so substract 1 to convert it to the Map coordinate system that starts at (0, 0)
	if origin == 1:
		x = x - 1
		y = y - 1
	
	# Convert the pixel coordinates to world coordinates
	world = map.pixel_to_world(x * pixel, y * pixel)
	
	# Convert the world coordinates to Heliographic Stonyhurst
	stonyhurst = world.transform_to(frames.HeliographicStonyhurst)
	
	return stonyhurst.lon.degree, stonyhurst.lat.degree,


def get_stats(map, region, region_stat):
	'''Return a region stats'''
	
	# Convert the center pixel coordinates to Heliographic Stonyhurst
	center_lon, center_lat = get_heliographic_coordinate_stonyhurst(map, float(region_stat['XCENTER']), float(region_stat['YCENTER']), origin = 1)
	
	stats = {
		'Id': int(region['ID']),
		'Color': int(region['TRACKED_COLOR']),
		'Date observation': region['DATE_OBS'] + 'Z',
		'Center longitude': center_lon,
		'Center latitude': center_lat,
		'Raw area': float(region_stat['RAW_AREA']),
		'Raw area uncertainty': float(region_stat['RAW_AREA_UNCERTAINITY']),
		'Area at disk center': float(region_stat['AREA_ATDISKCENTER']),
		'Area at disk center uncertainty': float(region_stat['AREA_ATDISKCENTER_UNCERTAINITY']),
		'Clipped spatial': region_stat['CLIPPED_SPATIAL'],
		# 'Number good pixels': region_stat['NUMBER_GOOD_PIXELS'],
	}
	
	return stats


def get_CHMap_stats(map_path):
	'''Return all the requested stats in a SPoCA CHMap'''
	# Open the FITS file
	hdus = fits.open(map_path)
	
	# Create a sunpy Map for converting the pixel coordinates
	image_hdu = hdus[image_hdu_name]
	map = Map(image_hdu.data, image_hdu.header)
	
	# Get regions by id
	regions_hdu = hdus[region_hdu_name]
	regions = {
		region['ID']: region
		for region in regions_hdu.data
	}
	
	# Get region stats by id
	region_stats = {
		region_stat['ID']: region_stat
		for region_stat in hdus[region_stats_hdu_name].data
	}
	
	# Create the stats list
	stats_list = list()
	
	for id, region in regions.items():
		stats_list.append(get_stats(map, region, region_stats[id]))
	
	return stats_list


# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CHMap and write corresponding events to JSON files')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--output_file', '-o', default = './stats.csv', help = 'The output file for the CSV file')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The file path to a tracked SPoCA CHMap')
	
	args = parser.parse_args()
	
	# Setup the logging
	logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s')
	
	headers = None
	with open(args.output_file, 'wt', encoding='UTF-8', newline='') as f:
		csv = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
		
		for map_path in args.maps:
			logging.info('Parsing map %s', map_path)
			
			# Get all stats from the CHMap
			stats_list = get_CHMap_stats(map_path)
			
			# Get the headers
			if headers is None and stats_list:
				headers = list(stats_list[0].keys())
				csv.writerow(headers)
			
			# Write the stats
			for stats in stats_list:
				csv.writerow(stats[header] for header in headers)
