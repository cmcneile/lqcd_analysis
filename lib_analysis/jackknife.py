##
##  Common jackknie routines
##

import math

def jackknife(jloop,nsample):
  jmean = 0.0
  for isample in  range(0,nsample) :
    jmean += jloop[isample]

  jmean  /= nsample

  jtot = 0.0
  for isample in  range(0,nsample) :
    ttt   = (jloop[isample] - jmean )
    jtot +=  ttt * ttt

  return math.sqrt( (nsample - 1.0)/(1.0*nsample) * jtot     )
