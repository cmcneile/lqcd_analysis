from numpy import *
import re
import math
import os.path
import sys

import pickle  


print "Starting to read the file "

with open('data.pickle', 'rb') as f:
# The protocol version used is detected automatically, so we do not
# have to specify it.
  eigstore = pickle.load(f)


print "The data has been read"
tmp = eigstore.shape

print "Dimensions = " , tmp[0] ,  tmp[1] ,  tmp[2] 

maxeig = tmp[0]
tval = tmp[2]

print "Summary"
for ieig in range(0,maxeig):
   print "Eigenvalue = " , ieig
   for tp in range(0,tval):
      print tp , eigstore[ieig,0,tp] , eigstore[ieig,1,tp] 


##from matplotlib import pylab
##from matplotlib.pyplot import *
from matplotlib import *

      
sys.exit(0)

