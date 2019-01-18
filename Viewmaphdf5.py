#####################################################################################################################
###                                       View maps from hdf5 files                                             #####
###                                                                                                             ##### 
### Authors E. Guimaraes and K. Fornazier                                                                       #####
#####################################################################################################################


import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

f  = h5py.File("Con.hdf5")
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[1]
data = list(f[a_group_key])

a = np.asarray(data)

hp.mollview(a[0,:])
plt.show()
#hp.mollview(a[9,:])
#plt.show()
