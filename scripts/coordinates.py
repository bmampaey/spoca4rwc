from astropy.units import pixel
from sunpy.map import Map
from sunpy.coordinates import frames
aia_file_name = '/data/SDO/public/AIA_HMI_1h_synoptic/aia.lev1.prepped/0193/2010/05/20/AIA.20100520_005954.0193.image_lev1_prepped.fits'
CH_map_file_name = 'CH_maps/20100520_000000.CHMap.fits'
aia = Map(aia_file_name)
ch_map = Map(CH_map_file_name)
ch_map.coordinate_frame
aia.coordinate_frame
aia.coordinate_system
ch_map.coordinate_system

c = ch_map.pixel_to_world(2048.5 * pixel, 2048.5 * pixel)
c.transform_to(frames.HeliographicStonyhurst)
