import numpy as np
import math as math
from writephrq import *

fldoc   = 0.01
fsom1   = 0.01
fsom2   = 0.02
fsom3   = 0.10
fmic    = 1.0e-5

sldoc   = 0.4

ffe3    = 0.01

kfera   = 0.5
kferh   = 0.8
kmega   = 0.3
kmegh   = 0.5

kdecay  = 0.05

fsom1o  = fsom1
fsom2o  = fsom2
fsom3   = fsom3
fferbo  = fmic*2.0 
fmeg    = fmic 

fldoco  = fldoc 
ffe3o   = ffe3

ffe3co  = ffe3o * 2.0
fldocco = fldoco 
fsom1co = fsom1o 
fsom2co = fsom2o
fferbco = fferbo 
fmegaco = fmeg
fmegh   = fmeg
 
totc = [0.045,  0.105, 0.104,  0.105,  0.074, 0.056]                #mol  total organic carbon
totw = [0.013588, 0.005854, 0.011788, 0.006379, 0.010690, 0.006620] #kg   water
tots = [1.41,    9.15,  3.21,   8.62,   4.31 , 8.38]                #g    soil dry mass
ph   = [5.02,    4.84,  5.21,   4.54,   5.23,  4.95]
cace = [6.370,  2.799, 0.057,  2.668,  1.026, 1.839]                #mM   acetate
cfe2 = [0.789, 22.234, 0.102, 22.973, 15.665, 7.177]                #mM   Fe
hdsp = [0.042528, 0.042528, 0.044005, 0.044005, 0.043575, 0.043575] #head space volume L
 
index = 0
writephrq('co', -2, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
writephrq('co',  4, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
writephrq('co',  8, totc[index], totw[index], tots[index], hdsp[index], ph[index], cace[index], cfe2[index], \
          ffe3co, fldocco, fsom1co, fsom2co, fsom3, kfera, kferh, kmega, kmegh, kdecay, fferbco, fmegaco, fmegh, sldoc)
 
