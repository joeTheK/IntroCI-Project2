# Joseph Kelley
# Verify fuzzLibrary membership functions using skfuzzy

import skfuzzy as fuzz
import numpy as np

from fuzzLibrary import *

#test membership functions

samples100 = np.linspace(0,100, 100)
samples1k = np.linspace(1, 100, 1000)

skfuzzGauss1 = fuzz.gaussmf(samples100, 50, 10)
skfuzzGauss2 = fuzz.gaussmf(samples1k, 50, 10)

#GAUSS MF

myGauss1 = gaussmf(samples100, 50, 10)
myGauss2 = gaussmf(samples1k, 50, 10)

print("Skfuzzy 100 samples and my gaussian mf average diff: {}".format(np.average(np.subtract(skfuzzGauss1, myGauss1))))
print("Skfuzzy 1000 samples and my gaussian mf average diff: {}".format(np.average(np.subtract(skfuzzGauss2, myGauss2))))

#TRAP MF

skfuzzTrap1 = fuzz.trapmf(samples100, [25,45,65,75])
skfuzzTrap2 = fuzz.trapmf(samples1k, [25,45,65,75])

myTrap1 = trapmf(samples100, [25,45,65,75])
myTrap2 = trapmf(samples1k, [25,45,65,75])

print("Skfuzzy 100 samples and my trapezoid mf average diff: {}".format(np.average(np.subtract(skfuzzTrap1, myTrap1))))
print("Skfuzzy 1000 samples and my trapezoid mf average diff: {}".format(np.average(np.subtract(skfuzzTrap2, myTrap2))))

skfuzzTri1 = fuzz.trimf(samples100, [0, 50, 75])
skfuzzTri2 = fuzz.trimf(samples1k, [0,50,75])

#TRIANGULAR MF

myTri1 = trimf(samples100, [0, 50, 75])
myTri2 = trimf(samples1k, [0, 50, 75])

print("Skfuzzy 100 samples and my triangle mf average diff: {}".format(np.average(np.subtract(skfuzzTri1, myTri1))))
print("Skfuzzy 1000 samples and my triangle mf average diff: {}".format(np.average(np.subtract(skfuzzTri2, myTri2))))