from numpy import *
import re
import math
import os.path
import sys

import pickle  


print "Starting to read the file "

with open('data/param.pickle', 'rb') as f:
# The protocol version used is detected automatically, so we do not
# have to specify it.
  Param = pickle.load(f)

print "Parameters of the correlators"
for kkk in Param.keys()  :
   print kkk , " ="  , Param[kkk]

##sys.exit()

with open('data/eigstore.pickle', 'rb') as f:
  eigstore = pickle.load(f)


with open('data/tvalues.pickle', 'rb') as f:
     tvalues = pickle.load(f)



print "The data has been read"
tmp = eigstore.shape

print "Dimensions = " , tmp[0] ,  tmp[1] ,  tmp[2] 

maxeig = tmp[0]
tval = tmp[2]

print "Summary"
for ieig in range(0,maxeig):
   print "Eigenvalue = " , ieig
   for tp in range(0,tval):
      print tvalues[tp] , eigstore[ieig,0,tp] , eigstore[ieig,1,tp] 


##from matplotlib import pylab
##from matplotlib.pyplot import *
##from matplotlib import *

import pylab
##from matplotlib.pyplot import *

pylab.ylim(ymax=1) # adjust the max leaving min unchanged
pylab.ylim(ymin=-0.5) # adjust the min leaving max unchanged

pylab.xlim(xmin=0) # adjust the min leaving max unchanged
pylab.xlim(xmax=7) # adjust the max leaving min unchanged

pylab.title('Glueball 0RPmR ', {'color':'k','fontsize':18})

pylab.ylabel('<G(t)G(t+1)> ', {'color':'k','fontsize':18})
pylab.xlabel('t', {'color':'k','fontsize':18})

pylab.errorbar(x=tvalues, y=eigstore[ieig,0,0:tval],yerr=eigstore[ieig,1,0:tval],fmt='bs' ,linewidth=2  )
pylab.savefig('EigMass.pdf',format="pdf")
pylab.show()


      
sys.exit(0)

