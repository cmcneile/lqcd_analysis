#
#  Utilities to block correlators
#

import os.path
import re
import math
from numpy import *


def block2_corr(corr,nosample,nt):

  dim = nosample/2
  block_corr       = zeros( (nt,dim) )

  for t in range(0,nt) :
    for ss in range(0,dim) :
      pt   = 2.0*ss
      pt_p = pt + 1
      block_corr[t,ss] = 0.5*(corr[t,pt] + corr[t,pt_p]  )


  return block_corr



def block4_corr(corr,nosample,nt):

  dim = nosample/4
  block_corr       = zeros( (nt,dim) )

  for t in range(0,nt) :
    for ss in range(0,dim) :
      pt   = 4.0*ss
      pt_p = pt + 1
      pt_q = pt + 2
      pt_r = pt + 3

      if pt_r < nosample :
         block_corr[t,ss] = 0.25*(corr[t,pt]+corr[t,pt_p]+corr[t,pt_q]+corr[t,pt_r])
      elif pt_q < nosample :
         block_corr[t,ss] = (1.0/3.0)*(corr[t,pt]+corr[t,pt_p]+corr[t,pt_q])
      elif pt_r < nosample :
         block_corr[t,ss] = (1.0/2.0)*(corr[t,pt]+corr[t,pt_p] )
      elif pt < nosample :
         block_corr[t,ss] = (1.0/2.0)*(corr[t,pt] )


  return block_corr

