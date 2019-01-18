#####################################################################################################################
#####################################################################################################################
###                                       Script Sum fits using hstck                                           #####
###                                                                                                             ##### 
### Authors  K. Fornazier                                                                                       #####
### Description: simple routine for summing up different fits files in one                                      #####
### DATE: January 2019                                                                                          #####
#####################################################################################################################
##                        ####   
#####################################################################################################################
from astropy.io import fits
from astropy.table import Table, hstack

t1 = Table.read('ame_cube_test.fits', format='fits')
t2 = Table.read('cmb_cube_test.fits', format='fits')
t3 = Table.read('foreground_cube_test.fits', format='fits')
t4 = Table.read('free_free_cube_test.fits', format='fits')
t5 = Table.read('point_sources_cube_test.fits', format='fits')
t6 = Table.read('synch_cube_test.fits', format='fits')


new = hstack([t1, t2, t3, t4, t5, t6 ])

new.write('combined_all_foregrounds.fits')
