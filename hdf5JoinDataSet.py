#####################################################################################################################
###                                       Summing up hdf5 files                                                #####
###                                                                                                             ##### 
### Authors E. Guimaraes and K. Fornazier                                                                       #####
#####################################################################################################################

import numpy as np
import astropy.io as astro
import h5py
from astropy.io import fits as pyfits
from astropy.table import Table
import os

#abre o hdf5 le os datasets e copia os dados para um dataset de soma
dataset=np.empty([50,196608]);

f = h5py.File('Con.hdf5', 'a')

for keys in f.keys():

 data=f[keys][()]
 dataset=np.append(dataset,data,axis=0)

#x = numpy.delete(x, (0), axis=0)

for i in range(49):
 dataset=np.delete(dataset, (i), 0)


f.create_dataset("soma", data=dataset)
f.flush()
f.close()
