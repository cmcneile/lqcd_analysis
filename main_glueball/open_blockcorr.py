
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

bwidth = 2

print "I am loading the data"


##verb = False
verb = True


## variables

## introduction stuff
print "Number of blocks = " , nblock
print "Number of timeslices  = " , Ntmax
print "Number of operators " , numop
print "Width of bin = " , bwidth


##  ----------------------------------------



from corr_util  import *

input = "input.txt" 
inamesTmp = load_names_text( input )

inames = sort_inputfles(inamesTmp)

noconfig = len(inames)
print "Number ofconfigs = " , noconfig

import h5py

print "Average over block widths of " , bwidth

bconfig = noconfig / bwidth

def create_outfile(ii, inames) :
   tmp = inames[ii].split('/')
   itmp = len(tmp)  - 1 

   otag = "binned/" +  tmp[itmp]
#   print "DEBUG " , otag
   return otag


for iconf in range(0,bconfig):
   glueball_corr       = zeros( (nblock,nblock,Ntmax,numop,numop,numbin ))
   for ib in range(0,bwidth):
     ii = ib + iconf*bwidth 
     ifile = inames[ii] 
     if verb :
        print "Reading from " ,  ifile
     fff =  read_header(ifile,False) 
     read_body_Ainc(fff,False,glueball_corr)

   glueball_corr   /= bwidth

   otag = create_outfile(ii, inames) 
   ofile = otag + "bwidth_" + str(bwidth)  +  "_block_no_" + str(iconf)
   if verb :
     print "Writing binned data to  " ,  ofile
   write_gball_corr(ofile,verb,glueball_corr) 
   

sys.exit(0) 

