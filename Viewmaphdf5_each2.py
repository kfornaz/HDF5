#####################################################################################################################
###                                      View mao hdf5 files                                                    #####
###                                                                                                             ##### 
### Authors E. Guimaraes and K. Fornazier                                                                       #####
#####################################################################################################################


import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

f  = h5py.File("Con.hdf5")
print("Keys: %s" % f.keys())
#a_group_key = list(f.keys())[0]

for keys in f.keys():
    data = list(f[keys])
    a = np.asarray(data)
    hp.mollview(a[0,:], title=keys)
    plt.show()
print(f.keys)
