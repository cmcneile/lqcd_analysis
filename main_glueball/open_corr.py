
from numpy import *
import re
import math
import os.path
import sys

from param import *
from glueUtil import *
from glueAnal import *
from glueVary import *

print "I am loading the data"

verb = False
##verb = True


## variables

## introduction stuff
print "Number of blocks = " , nblock
print "Number of timeslices  = " , Ntmax
print "Number of operators " , numop


##  ----------------------------------------

sys.path.append('/home/cmcneile/Gcorr_case3_new_rago/lib_potential')

from corr_util  import *

input = "input.txt" 
inames = load_names_text( input )


noconfig = len(inames)
print "Number ofconfigs = " , noconfig


glueball_corr       = zeros( (noconfig, nblock,nblock,Ntmax,numop,numop,numbin ))

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


maxeig = 3
tvalues = [  2 , 3 , 4, 5 , 6 , 7  ] 
tval = len(tvalues) 
eigstore = zeros( (maxeig,2,tval ))

tp = 0 
for ttt in tvalues: 
   eigstore[0:maxeig,0:2,tp]  = basic_vary_analysis(ttt,noconfig,verb,maxeig,glueball_corr)
   tp += 1
   
##basic_vary_analysis(3,noconfig,verb,maxeig,glueball_corr)
##basic_vary_analysis(4,noconfig,verb,maxeig,glueball_corr)
##basic_vary_analysis(5,noconfig,verb,maxeig,glueball_corr)
##basic_vary_analysis(6,noconfig,verb,maxeig,glueball_corr)
##basic_vary_analysis(7,noconfig,verb,maxeig,glueball_corr) 


print "End of python analysis"
sys.exit(0)

