"""
Routines to load glueball correlators into python.
"""
import sys
import struct

from param import *
##from space import *



##
##
##

def read_header(inn,verbose) :
    """
    Read the header from a new style glueball correlator.
    """
    magicnumber = 12345678
    names = [  "HEADERSIZE" , "COUNTER", "LX1" , "LX2" , "LX3" , "LX4", "NCOL" , "NUMBIN" , "BINWIDTH" , "NUM_GOP" ,  "NUM_SOP" , "NUM_TOP" , "IBLOK" ,  "LMAX" , "LMAXTWS" , "SVNREVISION" ]
    lnames = len(names)

    hdim = 1

    head = [] 
    count = 0 
    try:
        f = open(inn, "rb")
        bbb = "start"
        while bbb != ""  and count < hdim :
            bbb = f.read(8)
            # Do stuff with byte.
            vvv = struct.unpack('d',bbb)
            iii = int(vvv[0])
	    if count == 0 :
                hdim = iii

            if verbose :
                ccc = count + 1
                if count < lnames:
                    print "Header " , ccc , names[count] , vvv , iii
                else:
                    print "Header " , ccc , "CORR" , vvv , iii

            if count  == 9 and iii != numop :
                print "Mismatch of number of operators"
                raise SomeError("An error occurred")

            if count  == 12 and iii != nblock  :
                print "Mismatch of number of blocks"
                raise SomeError("An error occurred")

            if count  == 13 and iii != Ntmax  :
                print "Mismatch of number of blocks"
                raise SomeError("An error occurred")

            count = count + 1 


    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        raise
    except ValueError:
        print "Could not convert data to an integer."
        raise
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

#    print "Final entry in header " , iii
    if iii !=  magicnumber  :
      print "ERROR Does not match magic number " , magicnumber
      sys.exit(1) 

    return f



##
##  Older version
##

def read_header_old(inn,verbose) :
    """
    Read the header from an older style glueball correlator.
    """
    names = [  "LX1" , "LX2" , "LX3" , "LX4", "NCOL" , "NUMBIN" , "BINWIDTH" , "NUM_OP" , "IBLOK" ]
    head = [] 
    count = 0 
    try:
        f = open(inn, "rb")
        bbb = f.read(8)
        while bbb != ""  and count < 9 :
            # Do stuff with byte.
            vvv = struct.unpack('d',bbb)
            iii = int(vvv[0])
            if verbose :
                print "Header " , count , names[count] , vvv , iii
            bbb = f.read(8)
            if count  == 7 and iii != numop :
                print "Mismatch of number of operators"
                raise SomeError("An error occurred")

            if count  == 8 and iii != nblock  :
                print "Mismatch of number of blocks"
                raise SomeError("An error occurred")

            count = count + 1 


    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    return f

##
##
##

def read_body(f,verbose,jj,glueball_corr) :
    """
    Read the body of a glueball correlator file.
    
    """
    for ibin in range(0, numbin):
        for iopA in range(0,numop) :
            for iblockA in range(0, nblock) :
                for iopB in range(0,numop) : 
                    for iblockB in range(0, nblock) :
                        for t in range(0, Ntmax) :
                            
                            try:
                                bbb = f.read(8)
                            except IOError as e:
                                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                            except:
                                print "Unexpected error:", sys.exc_info()[0]
                                raise

                            vvv = struct.unpack('d',bbb)
                            if verbose :
                                print t, vvv[0]
            
                            glueball_corr[jj, iblockA,iblockB,t, iopA,iopB, ibin] = vvv[0]



    f.close()




##
##
##

def read_body_inc(f,verbose,jj,glueball_corr) :
    """
    Read the body of a glueball correlator file.
    Add the read in correlator to the existing correlator.
    This is used for blocking.
    """
    for ibin in range(0, numbin):
        for iopA in range(0,numop) :
            for iblockA in range(0, nblock) :
                for iopB in range(0,numop) : 
                    for iblockB in range(0, nblock) :
                        for t in range(0, Ntmax) :
                            
                            try:
                                bbb = f.read(8)
                            except IOError as e:
                                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                            except:
                                print "Unexpected error:", sys.exc_info()[0]
                                raise

                            vvv = struct.unpack('d',bbb)
                            if verbose :
                                print t, vvv[0]
            
                            glueball_corr[jj, iblockA,iblockB,t, iopA,iopB, ibin] = vvv[0]



    f.close()






##
##
##

def read_body_Ainc(f,verbose,glueball_corr) :
    """
    Read the body of a glueball correlator file.
    Add the read in correlator to the existing correlator.
    This is used for blocking.
    """
    for ibin in range(0, numbin):
        for iopA in range(0,numop) :
            for iblockA in range(0, nblock) :
                for iopB in range(0,numop) : 
                    for iblockB in range(0, nblock) :
                        for t in range(0, Ntmax) :
                            
                            try:
                                bbb = f.read(8)
                            except IOError as e:
                                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                            except:
                                print "Unexpected error:", sys.exc_info()[0]
                                raise

                            vvv = struct.unpack('d',bbb)
                            if verbose :
                                print t, vvv[0]
            
                            glueball_corr[iblockA,iblockB,t, iopA,iopB, ibin] = vvv[0]



    f.close()



##
##
##

def print_glueball(ii, glueball_corr) :
    """
    Print the glueball correlators to the screen.
    The correlator data structure includes all configurations
    """
    print "******************************"
    print "Correlator " , ii
    for iblock in range(0, numbin):
        for iopA in range(0,numop) :
            for iblockA in range(0, nblock) :
                for iopB in range(0,numop) : 
                    for iblockB in range(0, nblock) :
                        for t in range(0, Ntmax) :
                            
                            print glueball_corr[ii,iblockA,iblockB,t, iopA,iopB, iblock]




##
##
##

def print_glueball_A(ii, glueball_corr) :
    """
    Print the glueball correlators to the screen.
    The correlator data structure includes only ONE  configuration.
    """
    print "******************************"
    print "Correlator " , ii
    for iblock in range(0, numbin):
        for iopA in range(0,numop) :
            for iblockA in range(0, nblock) :
                for iopB in range(0,numop) : 
                    for iblockB in range(0, nblock) :
                        for t in range(0, Ntmax) :
                            
                            print glueball_corr[ii,iblockA,iblockB,t, iopA,iopB, iblock]





