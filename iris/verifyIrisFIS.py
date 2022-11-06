# Joseph Kelley
# Implements ways to verify Iris FIS for project 2: part 2

import sys
sys.path.insert(0, 'PATH TO fuzzLibrary')

from fuzzLibrary import *
from irisFIS import *

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# test accuracy goes through every data point in iris and checks if
# irisFIS1 returns the correct class per input.
# returns a list of incorrect inputs and their index in the dataset
def testAccuracy():
    incorrect = []
    pos = []
    for i in range(150):
        test = irisFIS1(iris.data[i])
        if(test != iris.target[i]):
            incorrect.append(iris.data[i])
            pos.append(i)
    return incorrect, pos


missed, pos = testAccuracy()

# prepare data to be plotted
def getData(arr, data):
    return [item[data] for item in arr]

missed_sepalL = getData(missed, 0)
missed_sepalW = getData(missed, 1)
missed_petalL = getData(missed, 2)
missed_petalW = getData(missed, 3)

missed_class = []
for i in pos:
    missed_class.append(iris.target[i])

#plot Incorrectly Classified inputs in 
axisLabels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
dataToPlot = [missed_sepalL, missed_sepalW, missed_petalL, missed_petalW]
fig, ax = plt.subplots(4,4)

for i in range(4):
    for j in range(4):
        if i != 3:
            ax[i][j].tick_params(bottom=False, labelbottom=False)
        if j != 0:
            ax[i][j].tick_params(left=False, labelleft=False)
        if i == j:
            ax[i][j].text(0, 0, axisLabels[i])
            if i == 0:
                ax[i][j].axis(ymin = 0, ymax=max(dataToPlot[i]))
            if i == 3:
                ax[i][j].axis(xmin = 0, xmax=max(dataToPlot[i]))
            continue

        ax[i][j].scatter(dataToPlot[j], dataToPlot[i], c=missed_class, s=5)
        
plt.show()

# the calls below were for the purpose of getting graphs for results section of paper.
#irisFIS1(iris.data[0], graphInVal=1, name1="irisRulesGraph01", name2="irisConsGraph01")
#irisFIS1(missed[0], graphInVal=1, name1="irisRulesGraph02", name2="irisConsGraph02")
#irisFIS1(missed[3], graphInVal=1, name1="irisRulesGraph03", name2="irisConsGraph03")
