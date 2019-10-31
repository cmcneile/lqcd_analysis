"""
Some basic analysis of the Glueball correlators.
"""

##
##  Glueball analysis
##

import sys
import struct

##sys.path.append('/home/cmcneile/production_runs/OpenBC_O2/correlators/Gcorr_case3_new_rago/python_analysis/lib_potential')
##sys.path.append('/home/cmcneile/Gcorr_case3_new_rago/lib_potential')

from param import *
from jackknife import *


##
##
##

def plotcorr_glueball(tag,iop,ib, noconfig,glueball_corr) :
    """
    Basic jacknife analysis of the glueball correlarors as a function of time.
    The correlator is diahonal in the operators and smearing basis.
    """

    tmp = zeros( (noconfig) )

    print ("DIAGONAL" , tag ,   "op=" , iop , " bin=" , ib)
    ibin = 0 
    for t in range(0, Ntmax) :
        mm = 0.0
        for iconfig in range(0,noconfig ) :
            tmp[iconfig]  =  glueball_corr[iconfig,ib,ib,t, iop,iop, ibin]
            mm = mm + tmp[iconfig]        
        mm = mm / noconfig
        jerr = jackknife(tmp,noconfig)

        print (t, mm, jerr)





