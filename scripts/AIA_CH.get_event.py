import logging
import argparse
from astropy.units import pixel
from astropy.io import fits
from sunpy.map import Map
from sunpy.coordinates import frames

from AIA_CH_schema import CoronalHole, CoronalHoleDetection

# Default path for the log file
log_file =  '/home/rwceventdb/log/AIA_CH.get_event.log'

# The CH map HDU that contains the image
image_hdu = 'CoronalHoleMap'

# The CH map HDU that contains the regions
region_hdu = 'Regions'

# The CH map HDU that contains the chaincodes
chaincode_hdu = 'ChainCodes'

# The CH map HDU that contains the region stats
region_stats_hdu = 'AIA_193_CoronalHoleStats'


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
		image = hdus[image_hdu]
		regions = hdus[region_hdu]
		chaincodes = hdus[chaincode_hdu]
		region_stats = hdus[region_stats_hdu]
		hdus.close()
		
		# Create a sunpy Map for converting the pixel coordinates
		map = Map(image.data, image.header)
		
		for region in regions:
			coronal_hole_detection = CoronalHoleDetection(Provider = CoronalHole._Provider_enum['+Provider_KSO'])



aia_file_name = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/0193/2010/05/20/AIA.20100520_005954.0193.image_lev1_prepped.fits'
CH_map_file_name = 'CH_maps/20100520_000000.CHMap.fits'
c = ch_map.pixel_to_world(2048.5 * pixel, 2048.5 * pixel)
c.transform_to(frames.HeliographicStonyhurst)
