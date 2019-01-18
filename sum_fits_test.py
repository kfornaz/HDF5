#####################################################################################################################
#####################################################################################################################
###                                       Sum Fits Test                                                        #####
###                                                                                                             ##### 
#####################################################################################################################
#####################################################################################################################

#%%
# Generally you would store the filename as string but in case you
# have no suitable FITS files you can use the ones shipped with Astropy
# like this:
from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath('/home/karin/Desktop/Foregrounds/output/cmb_cube_test.fits')

hdul = fits.open('/home/karin/Desktop/Foregrounds/output/cmb_cube_test.fits')


#%%
hdul.info()


#%%
hdul2 = fits.open('path/ame_cube_test.fits')


#%%
hdul2.info()


#%%
hdu_list = fits.open('path/cmb_cube_test.fits', memmap=True)


#%%
hdu_list.info()


#%%
from astropy.table import Table

evt_data = Table(hdu_list[0].data)


