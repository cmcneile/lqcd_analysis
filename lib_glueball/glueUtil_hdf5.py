"""
Routines to load glueball correlators in the hdf5 format
"""
import sys
import struct

from param import *

import h5py



def write_gball_corr(fname,verbose,glueball_corr) :
    """
    Write the glueball correlator file in hdf5 format.
    """

    with h5py.File(fname, 'w') as hf:
     	 hf.create_dataset('gballcorr', data=glueball_corr)


    if verbose :
       print "Data written to " , fname , " in hdf5 format"



def read_gball_corr(fname,verbose) :
    """
    Read the glueball correlator file in hdf5 format.
    """

##    glueball_corr = zeros( (nblock,nblock,Ntmax,numop,numop,numbin ))

    with h5py.File(fname, 'r') as hf:
     	 data           = hf.get('gballcorr')
         glueball_corr  = array(data)

    if verbose :
       print "Data read from " , fname , " in hdf5 format"

    return glueball_corr
