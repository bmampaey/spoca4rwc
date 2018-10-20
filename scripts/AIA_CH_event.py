import logging
import argparse
from astropy.units import pixel
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames

from CH_schema import CoronalHoleDetection, _HeliographicCoordinate, _HeliographicCoordinate_Stonyhurst, _HeliographicCoordinate_Carrington, _SolarSurface_BoundingBox, _SolarSurface_Area, SPOCA_CoronalHole

# Default path for the log file
log_file =  '/home/rwceventdb/log/AIA_CH_get_event.log'

# The CH map HDU that contains the image
image_hdu_name = 'CoronalHoleMap'

# The CH map HDU that contains the regions
region_hdu_name = 'Regions'

# The CH map HDU that contains the chaincodes
chaincode_hdu_name = 'ChainCodes'

# The CH map HDU that contains the region stats
region_stats_hdu_name = 'AIA_193_CoronalHoleStats'

def pixel_to_stonyhurst(map, x, y):
	'''Convert pixel coordinates to Stonyhurst coordinates'''
	pixel = map.pixel_to_world(x * pixel, y * pixel)
	stonyhurst = pixel.transform_to(frames.HeliographicStonyhurst)
	return stonyhurst.lat, stonyhurst.lon

def pixel_to_carrington(map, x, y):
	'''Convert pixel coordinates to Carrington coordinates'''
	pixel = map.pixel_to_world(x * pixel, y * pixel)
	carrington = pixel.transform_to(frames.HeliographicCarrington)
	return carrington.lat, carrington.lon

def get_coronal_hole_detection(map, region, region_stat, chaincode):
	latitude, longitude = pixel_to_stonyhurst(map, region_stat['XCENTER'], region_stat['YCENTER'])
	stonyhurst = _HeliographicCoordinate_Stonyhurst(
		Latitude = latitude,
		Longitude = longitude,
	)
	
	latitude, longitude = pixel_to_carrington(map, region_stat['XCENTER'], region_stat['YCENTER'])
	carrington = _HeliographicCoordinate_Carrington(
		Latitude = latitude,
		Longitude = longitude,
	)
	
	location = _HeliographicCoordinate(
		Carrington = carrington,
		Stonyhurst = stonyhurst,
		Time = region['DATE_OBS'],
	)
	
	bounding_box = _SolarSurface_BoundingBox(
		LatitudeS = None,
		LongitudeE = None,
		LatitudeN = None,
		LongitudeW = None,
	)
	
	area = _SolarSurface_Area(
		Mm = region_stat['AREA_ATDISKCENTER'],
		SH = None,
		Arcsec = None,
		error = region_stat['AREA_ATDISKCENTER_UNCERTAINITY'],
	)
	
	contour = list()
	for x, y in zip(*chaincode):
		if x == 0 and y == 0:
			break
		else:
			latitude, longitude = pixel_to_stonyhurst(map, x, y)
			stonyhurst = _HeliographicCoordinate_Stonyhurst(
				Latitude = latitude,
				Longitude = longitude,
			)
			contour.append(stonyhurst)
	
	coronal_hole_detection = CoronalHoleDetection(
		Location = location,
		CoronalHole = None,
		BoundingBox = bounding_box,
		Area = area,
		Contour = contour,
		Provider = CoronalHoleDetection._Provider_enum['+Provider_KSO'],
	)
	
	return coronal_hole_detection

def get_spoca_coronal_hole(region_stat):
	spoca_coronal_hole = SPOCA_CoronalHole(
		Min = region_stat['MIN_INTENSITY'],
		FirstQuartile =  region_stat['LOWERQUARTILE_INTENSITY'],
		Var =  region_stat['VARIANCE'],
		Max =  region_stat['MAX_INTENSITY'],
		Mean =  region_stat['MEAN_INTENSITY'],
		Skewness =  region_stat['SKEWNESS'],
		Kurtosis =  region_stat['KURTOSIS'],
		Median =  region_stat['MEDIAN_INTENSITY'],
		ThirdQuartile =  region_stat['UPPERQUARTILE_INTENSITY'],
		DetectionTime =  region_stat['DATE_OBS'],
	)
	
	return spoca_coronal_hole

# Start point of the script
if __name__ == '__main__':
	
	# Get the arguments
	parser = argparse.ArgumentParser(description = 'Extract the regions from a CH map and create corresponding events')
	parser.add_argument('--debug', '-d', default = False, action = 'store_true', help = 'Set the logging level to debug')
	parser.add_argument('--log_file', '-l', default = log_file, help = 'The file path of the log file')
	parser.add_argument('maps', metavar = 'MAP', nargs='+', help = 'The path to a SPoCA map')
	
	args = parser.parse_args()
	
	# Setup the logging
	if args.debug:
		logging.basicConfig(level = logging.DEBUG, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	else:
		logging.basicConfig(level = logging.INFO, format='%(asctime)s : %(levelname)-8s : %(message)s', filename=args.log_file)
	
	for map_path in args.maps:
		hdus = fits.open(map_path)
		image_hdu = hdus[image_hdu_name]
		regions_hdu = hdus[region_hdu_name]
		chaincodes_hdu = hdus[chaincode_hdu_name]
		region_stats_hdu = hdus[region_stats_hdu_name]
		
		# Create a sunpy Map for converting the pixel coordinates
		map = Map(image_hdu.data, image_hdu.header)
		
		# Get the data of the regions
		regions = {region['ID']: region for region in regions_hdu.data}
		region_stats = {region_stat['ID']: region_stat for region_stat in region_stats_hdu.data}
		chaincodes = {id: (chaincodes_hdu.data['X%07d' % id], chaincodes_hdu.data['Y%07d' % id]) for id in regions_hdu.data['ID']}
		
		for id, region in regions.items():
			coronal_hole_detection = get_coronal_hole_detection(map, region, region_stats[id], chaincodes[id])
