
from numpy import *
import re
import math
import os.path
import sys

from param import *
from glueUtil import *
from glueAnal import *
from glueVary import *
from glueUtil_hdf5 import *

bwidth = 4 

print "I am loading the data"


##verb = False
verb = True


## variables

## introduction stuff
print "Number of blocks = " , nblock
print "Number of timeslices  = " , Ntmax
print "Number of operators " , numop


##  ----------------------------------------

##sys.path.append('/home/cmcneile/Gcorr_case3_new_rago/lib_potential')

from corr_util  import *

input = "input.txt" 
inames = load_names_text( input )


noconfig = len(inames)
print "Number ofconfigs = " , noconfig

import h5py

print "Average over block widths of " , bwidth

bconfig = noconfig / bwidth


for iconf in range(0,bconfig):
   glueball_corr       = zeros( (bconfig, nblock,nblock,Ntmax,numop,numop,numbin ))
   for ib in range(0,bwidth):
     ii = ib + iconf*bwidth 
     ifile = inames[ii] 
     if verb :
        print "Reading from " ,  ifile


   glueball_corr   /= bwidth


   tmp = inames[ii].split('/')
   itmp = len(tmp)  - 1 

   otag = "binned/" +  tmp[itmp]
   print "DEBUG " , otag
   ofile = otag + "bwidth_" + str(bwidth)  +  "_block_no_" + str(iconf)
   if verb :
     print "Writing binned data to  " ,  ofile
   write_gball_corr(ofile,verb,glueball_corr) 
   

sys.exit(0) 

