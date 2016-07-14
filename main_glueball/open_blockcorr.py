
from numpy import *
import re
import math
import os.path
import sys

from param import *
from glueUtil import *
from glueAnal import *
from glueVary import *


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



print "Average over block widths of " , bwidth

bconfig = noconfig / bwidth
glueball_corr       = zeros( (bconfig, nblock,nblock,Ntmax,numop,numop,numbin ))

for iconf in range(0,bconfig):
   for ib in range(0,bwidth):
     ii = ib + iconf*bwidth 
     ifile = inames[ii] 
     if verb :
        print "Reading from " ,  ifile

glueball_corr   /= bwidth

sys.exit(0) 

##  ----------------------------------------
ii = 0
for ifile in inames:
   if verb :
      print "Reading from " ,  ifile

   tmp = ifile.split('/', 2)
   cname = tmp[2]
   
#   print "Reading the header "
   fff =  read_header(ifile,verb) 
#   sys.exit(0)
#   verb = False

#   print "Reading the data"
   read_body(fff,verb,ii, glueball_corr)
#   print "Data has been read"
   ii = ii + 1 



##plotcorr_glueball(0,0, noconfig,glueball_corr) 
##plotcorr_glueball(10,4, noconfig,glueball_corr)
##plotcorr_glueball(15,4, noconfig,glueball_corr)
##print cname
##plotcorr_glueball(cname, 18,4, noconfig,glueball_corr) 


basic_vary_analysis(2,noconfig,verb, glueball_corr)
basic_vary_analysis(3,noconfig,verb, glueball_corr)
basic_vary_analysis(4,noconfig,verb, glueball_corr)
basic_vary_analysis(5,noconfig,verb, glueball_corr)
basic_vary_analysis(6,noconfig,verb, glueball_corr)
basic_vary_analysis(7,noconfig,verb, glueball_corr) 


print "End of python analysis"
sys.exit(0)

