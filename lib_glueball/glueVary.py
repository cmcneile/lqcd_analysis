
import sys
import struct

from param import *
##from space import *

from numpy import linalg as LA
from numpy import *

##sys.path.append('/home/cmcneile/Gcorr_case3_new_rago/lib_potential')
from jackknife import *

##
##
##

def compute_full_vary(tvary,noconfig,glueball_corr) :



  print "Eigenvalue analysis t = " , tvary

  dim = nblock * numop
  
  vary_corr       = zeros( (dim,dim ))
  for i5 in range(0,numop) :
    for i4 in range(0, nblock) :
      for i3 in range(0,numop) : 
        for i2 in range(0, nblock) :
          ii = i2 + nblock * i3 
          jj = i4 + nblock * i5
          vary_corr[ii,jj] = 0.0

          for i6 in range(0, numbin):
            for iconf in range(0,noconfig):
              vary_corr[ii,jj] = vary_corr[ii,jj] + glueball_corr[iconf,i4,i2,tvary, i5,i3, i6] 

          vary_corr[ii,jj] = vary_corr[ii,jj] / (numbin *  noconfig) 
              
# .         print "Vary[" , ii,jj,"]= " , vary_corr[ii,jj]  
#  print "Making the matrix symmetric"
  for ii in range(0 , dim):
    for jj in range(ii+1, dim) :
      tmp = (vary_corr[ii,jj]   + vary_corr[jj,ii]  ) / 2.0 
      vary_corr[ii,jj] = tmp
      vary_corr[jj,ii] = tmp


  return vary_corr


##
##
##

def compute_jack_vary(jomit, tvary,noconfig,glueball_corr) :


  dim = nblock * numop

  jdim = numbin *  noconfig - 1 
  
  vary_corr       = zeros( (dim,dim ))
  for i5 in range(0,numop) :
    for i4 in range(0, nblock) :
      for i3 in range(0,numop) : 
        for i2 in range(0, nblock) :
          ii = i2 + nblock * i3 
          jj = i4 + nblock * i5
          vary_corr[ii,jj] = 0.0

          for i6 in range(0, numbin):
            for iconf in range(0,jomit):
              vary_corr[ii,jj] = vary_corr[ii,jj] + glueball_corr[iconf,i4,i2,tvary, i5,i3, i6] 

            for iconf in range(jomit+1,noconfig):
              vary_corr[ii,jj] = vary_corr[ii,jj] + glueball_corr[iconf,i4,i2,tvary, i5,i3, i6] 

              
          vary_corr[ii,jj] = vary_corr[ii,jj] / (jdim) 
              
# .         print "Vary[" , ii,jj,"]= " , vary_corr[ii,jj]  
#  print "Making the matrix symmetric"
  for ii in range(0 , dim):
    for jj in range(ii+1, dim) :
      tmp = (vary_corr[ii,jj]   + vary_corr[jj,ii]  ) / 2.0 
      vary_corr[ii,jj] = tmp
      vary_corr[jj,ii] = tmp


  return vary_corr




##
##
##

def basic_vary_analysis(tvary,noconfig,verb,  maxeig , glueball_corr) :

  print "Eigenvalue analysis t = " , tvary
##  maxeig = 5
##the second index is for mean and error  
  eig_ans       = zeros( (maxeig,2 ))

  jeig = zeros( (maxeig,noconfig) )


  
  dim = nblock * numop
  print "Dimension of vary matrix = " , dim
  
  vary_corr       =  compute_full_vary(tvary,noconfig,glueball_corr) 
  print "Start of eigenvalue analysis"
  w, v = LA.eig(vary_corr)

  if verb :
    for ii in range(0,maxeig) :
      print "FEIG[" , ii , "]= " , w[ii] 

  print "Start of Jackknife analysis"
  for iconfig in range(0 , noconfig)  :
    jvary_corr = compute_jack_vary(iconfig, tvary,noconfig,glueball_corr)
    jw, v = LA.eig(jvary_corr)

    for kk in range(0,maxeig)  : 
       jeig[kk,iconfig] = jw[kk]
      

##
##
##
  teig = zeros( (noconfig) )

  for kk in range(0,maxeig)  : 
    for iconfig in range(0 , noconfig)  :
      teig[iconfig] = jeig[kk,iconfig]
    jerr = jackknife(teig,noconfig)    
    print "EIG[",tvary,",",kk ,"]= " , w[kk] , jerr 
    eig_ans[kk,0] =  w[kk]
    eig_ans[kk,1] =  jerr
    
  print "End of jackknife analysis"

  return eig_ans 
