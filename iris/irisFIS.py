# Joseph Kelley
# Main code to implement Iris FIS for project 2: part 2

import sys
sys.path.insert(0, 'PATH TO fuzzLibrary')

from fuzzLibrary import *

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# constants for last index of each class
C0END = 49
C1END = 99
C2END = 149

# creates consequent membership graphs
# three rectangles side by side to classify without undefined values
x_classes = np.linspace(0, 1, 100)
setosamf = trapmf(x_classes, [0,0,1/3,1/3])
versimf = trapmf(x_classes, [1/3,1/3,2/3,2/3])
vergimf = trapmf(x_classes, [2/3,2/3,1,1])

#seperate iris data into different data sets
sepalLen_data = iris.data[:, 0]
sepalWid_data = iris.data[:, 1]
petalLen_data = iris.data[:, 2]
petalWid_data = iris.data[:, 3]

# membership functions
x_petalLen = np.linspace(0,np.max(petalLen_data), 100)
    
petalLen_lo = trapmf(x_petalLen, [0,0,0,2.5])
petalLen_md = trapmf(x_petalLen, [2.5, np.min(petalLen_data[C0END + 1:C1END]), np.min(petalLen_data[C1END+1:C2END]), np.max(petalLen_data[C0END + 1:C1END])])
petalLen_hi = trapmf(x_petalLen, [np.min(petalLen_data[C1END+1:C2END]), np.max(petalLen_data[C0END + 1:C1END]), np.max(petalLen_data), np.max(petalLen_data)])

x_petalWid = np.linspace(0, np.max(petalWid_data), 100)

petalWid_lo = trapmf(x_petalWid,[0, np.min(petalWid_data[C0END + 1:C1END]), np.min(petalWid_data[C1END+1:C2END]), np.max(petalWid_data[C0END + 1:C1END])])
petalWid_hi = trapmf(x_petalWid,[np.min(petalWid_data[C1END+1:C2END]), np.max(petalWid_data[C0END + 1:C1END]), np.max(petalWid_data[C1END + 1:C2END]), np.max(petalWid_data)])

# function that takes in an input list of 4 floats from the iris data.
# has 3 optional paramaters to graph and save graphs as name1 and name2
# returns the class of input 0 - Setosa, 1 - Versicolour, 2 - Virginica
def irisFIS1(input, graphInVal = 0, name1='', name2=''):

    #if petalLen lo then setosa
    rule1 = corrMin([memberVal(x_petalLen, petalLen_lo, input[2]),setosamf])

    #if petalLen md AND petalWid lo then versi
    temp = ANDop([memberVal(x_petalLen, petalLen_md, input[2]), memberVal(x_petalWid, petalWid_lo, input[3])])
    rule2 = corrMin([temp, versimf])

    #if petalLen hi AND petalWid hi then virgi
    temp = ANDop([memberVal(x_petalLen, petalLen_hi, input[2]), memberVal(x_petalWid, petalWid_hi, input[3])])
    rule3 = corrMin([temp, vergimf])

    # graph activated rules
    if graphInVal == 1:
        fig, ax = plt.subplots(2,1)
        ax[0].plot(x_petalLen, petalLen_lo)
        ax[0].plot(x_petalLen, petalLen_md)
        ax[0].plot(x_petalLen, petalLen_hi)
        ax[0].fill_between(x_petalLen, np.minimum(petalLen_lo, memberVal(x_petalLen, petalLen_lo, input[2])), alpha=0.4)
        ax[0].fill_between(x_petalLen, np.minimum(petalLen_md, memberVal(x_petalLen, petalLen_md, input[2])), alpha=0.4)
        ax[0].fill_between(x_petalLen, np.minimum(petalLen_hi, memberVal(x_petalLen, petalLen_hi, input[2])), alpha=0.4)

        ax[1].plot(x_petalWid, petalWid_lo)
        ax[1].plot(x_petalWid, petalWid_hi)
        ax[1].fill_between(x_petalWid, np.minimum(petalWid_lo, memberVal(x_petalWid, petalWid_lo, input[3])), alpha=0.4)
        ax[1].fill_between(x_petalWid, np.minimum(petalWid_hi, memberVal(x_petalWid, petalWid_hi, input[3])), alpha=0.4)
        plt.savefig(name1)
        plt.show()

    if np.average(rule1) > 0:
        aggregated = rule1
    else:
        aggregated = aggregate([rule1, rule2, rule3], 'max')
    result = centroidDefuzz(x_classes, aggregated)

    # graph resultant graph with aggreagation and centroid
    if graphInVal == 1:
        plt.plot(x_classes, setosamf)
        plt.plot(x_classes, versimf)
        plt.plot(x_classes, vergimf)
        plt.fill_between(x_classes, aggregated, alpha=0.4)
        plt.axvline(result)
        plt.savefig(name2)
        plt.show()


    if(memberVal(x_classes, setosamf, result) > 0):
        return 0
    elif(memberVal(x_classes, versimf, result) > 0):
        return 1
    elif(memberVal(x_classes, vergimf, result) > 0):
        return 2
    else:
        return -1
