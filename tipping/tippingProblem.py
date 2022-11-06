# Joseph Kelley
# Tipping problem implemented just like one on VCS
# and from this tutorial: https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem.html
# for the purpose of verifying fuzzLibrary functions

import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.insert(0, 'C:/Users/josep/OneDrive/Documents/MU Fall 2022/CS 4770/Fuzzy/code')

from fuzzLibrary import *

xRangeQual = np.arange(0,11,1)
xRangeServ = np.arange(0,11,1)
xRangeTip = np.arange(0,26,1)

qual_lo = trimf(xRangeQual, [0, 0, 5])
qual_md = trimf(xRangeQual, [0, 5, 10])
qual_hi = trimf(xRangeQual, [5, 10, 10])
serv_lo = trimf(xRangeServ, [0, 0, 5])
serv_md = trimf(xRangeServ, [0, 5, 10])
serv_hi = trimf(xRangeServ, [5, 10, 10])
tip_lo = trimf(xRangeTip, [0, 0, 13])
tip_md = trimf(xRangeTip, [0, 13, 25])
tip_hi = trimf(xRangeTip, [13, 25, 25])

fig, ax = plt.subplots(3,1)

ax[0].plot(xRangeQual, qual_lo)
ax[0].plot(xRangeQual, qual_md)
ax[0].plot(xRangeQual, qual_hi)
ax[0].set_title("Food Quality")

ax[1].plot(xRangeServ, serv_lo)
ax[1].plot(xRangeServ, serv_md)
ax[1].plot(xRangeServ, serv_hi)
ax[1].set_title("Service Quality")

ax[2].plot(xRangeTip, tip_lo)
ax[2].plot(xRangeTip, tip_md)
ax[2].plot(xRangeTip, tip_hi)
ax[2].set_title("Tip Percent")
plt.show()

#6.5, 9.8
foodQual = 6.5
serviceQual = 9.8

qual_loTest = memberVal(xRangeQual, qual_lo, foodQual)
qual_mdTest = memberVal(xRangeQual, qual_md, foodQual)
qual_hiTest = memberVal(xRangeQual, qual_hi, foodQual)

serv_loTest = memberVal(xRangeServ, serv_lo, serviceQual)
serv_mdTest = memberVal(xRangeServ, serv_md, serviceQual)
serv_hiTest = memberVal(xRangeServ, serv_hi, serviceQual)

fig, ax = plt.subplots(2,1)

ax[0].plot(xRangeQual, qual_lo)
ax[0].plot(xRangeQual, qual_md)
ax[0].plot(xRangeQual, qual_hi)
ax[0].fill_between(xRangeQual, np.minimum(qual_lo, qual_loTest), alpha = 0.4)
ax[0].fill_between(xRangeQual, np.minimum(qual_md, qual_mdTest), alpha = 0.4)
ax[0].fill_between(xRangeQual, np.minimum(qual_hi, qual_hiTest), alpha = 0.4)
ax[0].set_title("Food Quality")

ax[1].plot(xRangeServ, serv_lo)
ax[1].plot(xRangeServ, serv_md)
ax[1].plot(xRangeServ, serv_hi)
ax[1].fill_between(xRangeServ, np.minimum(serv_lo, serv_loTest), alpha = 0.4)
ax[1].fill_between(xRangeServ, np.minimum(serv_md, serv_mdTest), alpha = 0.4)
ax[1].fill_between(xRangeServ, np.minimum(serv_hi, serv_hiTest), alpha = 0.4)
ax[1].set_title("Service Quality")
plt.show()

# rule 1: bad food or bad serv then tip low
# rule 2: average serv then tip avg
# rule 3: good food or good serv tehn tip high

rule1 = corrMin([ORop([qual_loTest, serv_loTest]), tip_lo])
rule2 = corrMin([serv_mdTest, tip_md])
rule3 = np.fmin(np.maximum(qual_hiTest, serv_hiTest), tip_hi)

aggregated = aggregate([rule1, rule2, rule3], "max")
result = centroidDefuzz(xRangeTip, aggregated)

plt.plot(xRangeTip, tip_lo)
plt.plot(xRangeTip, tip_md)
plt.plot(xRangeTip, tip_hi)
plt.fill_between(xRangeTip, aggregated, alpha=0.4, color="b")
plt.axvline(result, color="b")
plt.title("Tip Level and Aggregateed Rules")
#plt.savefig('myTippingProblemResult')
plt.show()

print(result)