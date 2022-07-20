#!/usr/bin/env python3
import argparse
from astropy.io import fits


quality_bits = {
0	: 'FLAT_REC == MISSING (Flatfield data not available)',
1	: 'ORB_REC == MISSING (Orbit data not available)',
2	: 'ASD_REC == MISSING (Ancillary Science Data not available)',
3	: 'MPO_REC == MISSING (Master pointing data not available)',
4	: 'RSUN_LF == MISSING or X0_LF == MISSING or Y0_LF == MISSING (HMI Limb fit not acceptable)',
5	: '',
6	: '',
7	: '',
8	: 'MISSVALS > 0',
9	: 'MISSVALS > 0.01*TOTVALS',
10	: 'MISSVALS > 0.05*TOTVALS',
11	: 'MISSVALS > 0.25*TOTVALS',
12	: 'ACS_MODE != "SCIENCE" (Spacecraft not in science pointing mode)',
13	: 'ACS_ECLP == "YES" (Spacecraft eclipse flag set)',
14	: 'ACS_SUNP == "NO" (Spacecraft sun presence flag not set)',
15	: 'ACS_SAFE == "YES" (Spacecraft safemode flag set)',
16	: 'IMG_TYPE == "DARK" (Dark image)',
17	: 'HWLTNSET == "OPEN" or AISTATE == "OPEN" (HMI ISS loop open or  AIA ISS loop Open)',
18	: '(FID >= 1 and FID <= 9999) or (AIFTSID >= 0xC000)  (HMI Calibration Image or AIA Calibration Image)',
19	: 'HCFTID == 17 (HMI CAL mode image)',
20	: '(AIFCPS <= -20 or AIFCPS >= 100) (AIA focus out of range)',
21	: 'AIAGP6 != 0 (AIA register flag)',
22	: '',
23	: '',
24	: '',
25	: '',
26	: '',
27	: '',
28	: '',
29	: '',
30	: 'Quicklook image',
31	: 'Image not available'
}

def get_quality(filepath, hdu_id = None, quality_keyword = 'QUALITY', ignore_bits = [0, 1, 2, 3, 4, 8, 30]):
	'''Return the quality value of the file, with ignore_bits set to 0'''
	
	with fits.open(filepath) as hdus:
		if hdu_id is not None:
			header = hdus[hdu_id].header
		else:
			for hdu in hdus:
				header = hdu.header
				if quality_keyword in header:
					break
		quality = header[quality_keyword]
	
	for bit in ignore_bits:
		quality &= ~(1<<bit)
	
	return quality

def get_quality_errors(quality):
	'''Return the set of errors corresponding to the bits set in the quality value'''
	errors = set()
	for bit, msg in quality_bits.items():
		if quality & (1 << bit):
			errors.add(msg or 'Unknown error')
	return errors

# Start point of the script
if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='Test the quality of an AIA FITS file')
	parser.add_argument('filepath', help='The path to the fits files to test')
	parser.add_argument('--hdu-id', '-i', metavar = 'HDU ID', type = int, help='The HDU number that contains the quality keyword')
	parser.add_argument('--keyword', '-K', default='QUALITY', help='The name of the quality keyword')
	
	args = parser.parse_args()
	
	try:
		quality = get_quality(args.filepath, hdu_id = args.hdu_id, quality_keyword = args.keyword)
	except Exception as why:
		print('Error getting quality for file ', args.filepath, ':', why)
	else:
		if quality != 0:
			print('Quality is BAD')
			for error in get_quality_errors(quality):
				print(error)
		else:
			print('Quality is GOOD')
