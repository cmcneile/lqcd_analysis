
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
   print_glueball_A(ii, glueball_corr) 
   if ii == 3 :
     sys.exit(0)

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
   


print "Summary"
for ieig in range(0,maxeig):
   print "Eigenvalue = " , ieig
   for tp in range(0,tval):
      print tvalues[tp] , eigstore[ieig,0,tp] , eigstore[ieig,1,tp] 

print "Starting to create the plot"


##import pylab
##from matplotlib.pyplot import *


##pylab.errorbar(x=tvalues, y=eigstore[ieig,0,0:tval],xerr=eigstore[ieig,1,0:tval],fmt='bs' ,linewidth=2  )
##pylab.savefig('EigMass.pdf',format="pdf")
##pylab.show()


##
##  https://docs.python.org/3/library/pickle.html#data-stream-format
##
import pickle



with open('data/eigstore.pickle', 'wb') as f:
# Pickle the 'data' dictionary using the highest protocol available.
   pickle.dump(eigstore, f, pickle.HIGHEST_PROTOCOL)
       

with open('data/tvalues.pickle', 'wb') as f:
# Pickle the 'data' dictionary using the highest protocol available.
   pickle.dump(tvalues, f, pickle.HIGHEST_PROTOCOL)
       


   
##with open('data.pickle', 'rb') as f:
# The protocol version used is detected automatically, so we do not
# have to specify it.
##data = pickle.load(f)


print "End of python analysis"
sys.exit(0)

