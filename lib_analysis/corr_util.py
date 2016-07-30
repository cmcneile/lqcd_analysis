#
#  Utilities for analyzing correlators
#
#

import os.path
import re
import math


#
#  load the correlators
#

def count_sample2( dirname , tag ):

  print "Counting files in " , dirname
  f = os.listdir(dirname)
  L = []  

  for line in f:
     if re.search(tag,line) :
       print line
       L.append(line)

  return L


def count_sample( filename ):

  print "Counting  data in " , filename
  f = open(filename, 'r')
  
  isample = 0
  for line in f:
     isample = isample + 1

  f.close
  return isample


#  Load list of filenames from my old text format
#
#
def load_names_text( filename ):

  print "Loading list of filenames from " , filename
  f = open(filename, 'r')
  L = []
  
  isample = 0
  for line in f:
     L.append(line.rstrip('\n'))

  f.close
  return L


def load_corr(filename,corr,isample ):

  print "Loading data in " , filename
  f = open(filename, 'r')
  
  t = 0
  for line in f:
    
    corr[t,isample] = line.rstrip('\n')
    t = t + 1

  f.close
  return 


def load_corr2(filename,corr,isample,imass ):

  print "Loading data in " , filename
  f = open(filename, 'r')
  
  t = 0
  for line in f:
    
    corr[t,isample,imass] = line.rstrip('\n')
    t = t + 1

  f.close
  return 





def get_corr3(filename,mm1,mm2,mm3, corr, isample, tag ):

    print isample, " loading data from " , filename, " isample ", isample
    f = open(filename, 'r')
  
    for line in f:
      if re.match(tag,line) :
        tmp = re.split(' ', line) 
        if tmp[1] != "CORR"  and tmp[0] != "3POINT_TWIST"  :

          m1 = int(tmp[1])
          m2 = int(tmp[2])
          m3 = int(tmp[3])

          t = int(tmp[5])

          corrRE = tmp[7]
          corrIM = tmp[8]

#          print line
          if m1 == mm1 and m2 == mm2 and m3 == mm3 :
             corr[t,isample] = corrRE 


    f.close


##    Only the twist angle of the pion is non-zero
##
##
def get_corr3_twist(filename,mm1,mm2,mm3,tt3, corr, isample,tag ):

    print isample, " loading data from " , filename
    f = open(filename, 'r')

    tt2 = 0 

    for line in f:
      if re.match(tag,line)  :
        tmp = re.split(' ', line) 
        if tmp[1] != "CORR"  :

          m1 = int(tmp[1])
          m2 = int(tmp[2])
          m3 = int(tmp[3])

          t2 = int(tmp[5])
          t3 = int(tmp[6])

          t = int(tmp[8])

          corrRE = tmp[10]
          corrIM = tmp[11]

#          print line
          if m1 == mm1 and m2 == mm2 and m3 == mm3 and t2 == tt2 and t3 == tt3:
             corr[t,isample] = corrRE 


    f.close




def dump_corr(corr,nsample,nt):

  for ss in range(0,nsample) :
    print "Sample " , ss
    for tt in range(0,nt) :
        
        print tt, corr[tt,ss ]




def av_corr(corr,nosample,t,jsample):

  if jsample < 0 :
    dim = nosample
  else :
    dim = nosample - 1

  total = 0.0 
  for ss in range(0,nosample) :
      if ss !=  jsample :
        total += corr[t ,ss ]


  total /= dim

  return total




def av_corr_sum_t(corr,nosample,nt,jsample):

  if jsample < 0 :
    dim = nosample
  else :
    dim = nosample - 1

  total = 0.0 
  for t  in range(0,nt):
    for ss in range(0,nosample) :
      if ss !=  jsample :
        total += corr[t ,ss ]


  total /= dim

  return total




def av_corr2(corr,nosample,t,jsample,outer_sample):

  if jsample < 0 :
    dim = nosample
  else :
    dim = nosample - 1

  if outer_sample > 0 :
    dim = dim -1

  total = 0.0 
  for ss in range(0,nosample) :
      if ss !=  jsample and ss != outer_sample :
        total += corr[t ,ss ]

  total /= dim

  return total



#
#
#


def qsq(L, theta, mpi, mk):

  pi = 3.14159265359
  p = (2.0 * theta * pi) / L 

  qsqt = (mk - math.sqrt(mpi**2 + p**2 ) )**2  - p**2;

  return qsqt






def av_corr_mass(corr,nosample,t,jsample,imass):

  if jsample < 0 :
    dim = nosample
  else :
    dim = nosample - 1

  total = 0.0 
  for ss in range(0,nosample) :
      if ss !=  jsample :
        total += corr[t ,ss,imass ]

  total /= dim

  return total


def sort_inputfles(ifiles) :
  """
   Sort the file names in terms of the sweep numbe.
  """

  one = ifiles[0] 
  two  =  ifiles[1]

  print "One = " , one
  print "Two = " , two

  ll = len(one) 

  print "Length of one = " , ll

  for ii in range(0,ll):
    iip = ii + 1
    ptOne = one[ii:iip]
    ptTwo = two[ii:iip]
    if ptOne  != ptTwo :
      print "Mismach at " , ii
      ifront = ii 
      break

##
##  now remove any digits
##

  while ifront > 1 :
    ii = ifront - 1
    tmp = one[ii:ifront]
    if not tmp.isdigit() :
      break
    ifront = ifront - 1

  tagStart = one[0:ifront]

  print "Starting tag "  , tagStart


  lone = len(one) 
  llone = lone 

  ltwo = len(two) 

  while lone > ifront and ltwo > ifront  :
    ptOne = one[(lone-1):lone]
    ptTwo = two[(ltwo-1):ltwo]

    if ptOne != ptTwo :
      tagend = one[lone:llone]
      break

    lone = lone - 1 
    ltwo = ltwo - 1 

##
##  now remove the digits
##

  ii = 0 
  while ii < llone :
    iip = ii + 1 
    ptOne = tagend[ii:iip]
    if not ptOne.isdigit() :
      tmp = tagend[ii:len(tagend)]
      tagend = tmp 
      break
    ii = ii + 1


  print "Tag end = " , tagend


  sweepstore = [] 


  for ff in ifiles:
    print ff

    ffr = ff.replace(tagend, "")
    fffr = ffr.replace(tagStart, "")
   
    sweepstore.append(fffr)

    print fffr 
    print " "
   


  print "Sweep numbers "

  for ff in sweepstore :
    print ff



  inorder = sorted(sweepstore)

  ans = [] 
  for ff in inorder :

    fff = tagStart + ff + tagend
    ans.append(fff)

  return ans
