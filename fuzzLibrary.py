# Joseph Kelley
# Library of functions needed to implement a Fuzzy Inference System

from math import e
from math import exp
import numpy as np

# Membership Functions
def trapmf(x, abcd):
    toReturn = []
    for i in x:
        toReturn.append(max(min((i-abcd[0])/(abcd[1] - abcd[0]), 1, (abcd[3] - i)/(abcd[3] - abcd[2])), 0))
    return toReturn

def gaussmf(x, mu, sig):
    toReturn = []
    for i in x:
        toReturn.append(exp(-.5*(((i-mu)/sig)**2)))
    return toReturn

def trimf(x, abc):
    toReturn = []
    if abc[0] == abc[1]:
        abc[0] = abc[0] - 1
    for i in x:
        toReturn.append(max(min((i-abc[0])/(abc[1] - abc[0]), (abc[2]-i)/(abc[2]-abc[1])), 0))
    return toReturn

# returns the membership value on an input test, using linear interpolation
# from samples space x and membership function memvals
def memberVal(x, memVals, test):
    return np.interp(test, x, memVals)  

# aggregation, if method is not "max" or "sum" will return -1
def aggregate(toAgg, method):
    toReturn = toAgg[0]
    for i in range(len(toAgg) - 1):
        curr = toReturn
        comp = toAgg[i+1]

        if(method == "max"):
            toReturn = np.fmax(curr, comp)
        elif(method == "sum"):
            toReturn = np.asarray(curr) + np.asarray(comp)
        else:
            return -1
    
    return toReturn

# defuzzification function
def centroidDefuzz(x, mf):
    top = 0
    for x, y in zip(x, mf):
        top += x*y
    bott = np.sum(mf)

    return top / bott

# Operation Functions
def ANDop(toAnd):
    toReturn = toAnd[0]
    for i in range(1, len(toAnd)):
        toReturn = np.maximum(toReturn, toAnd[i])
    return toReturn

def ORop(toOr):
    toReturn = toOr[0]
    for i in range(1, len(toOr)):
        toReturn = np.minimum(toReturn, toOr[i])
    return toReturn

def corrMin(toCorr):
    toReturn = toCorr[0]
    for i in range(1, len(toCorr)):
        toReturn = np.fmin(toReturn, toCorr[i])
    return toReturn