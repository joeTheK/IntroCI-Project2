# Joseph Kelley
# Part 3 of project 2: create a non-classification FIS

import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.insert(0, 'C:/Users/josep/OneDrive/Documents/MU Fall 2022/CS 4770/Fuzzy/code')

from fuzzLibrary import *

# to answer: how stressed am I based on workload and upcoming dates?

# RULE SET
#if workload lo then stress lo
#if workload md and due dates far then md
#if workload hi and due dates close then stress high

#workload is measured in # of hours of work
#due dates is measured in days between now and due date
#stress is measure on 1-10

# Membership Functions
workSamples = np.linspace(0, 20, 100)
dateSamples = np.linspace(0, 14, 100)
stressSamples = np.linspace(-4, 15, 100)

work_lo = trapmf(workSamples, [0,0,5,8])
work_md = trapmf(workSamples, [7,10,13,14])
work_hi = trapmf(workSamples, [13,17,20,20])

date_far = trapmf(dateSamples, [5,8,14,14])
date_close = trapmf(dateSamples, [0,0,4,7])

stress_lo = trimf(stressSamples, [-4,0,4])
stress_md = trimf(stressSamples, [3,5,7])
stress_hi = trapmf(stressSamples, [5,8,10,15])

# plot membership functions
fig, ax = plt.subplots(2,1)

ax[0].plot(workSamples, work_lo)
ax[0].plot(workSamples, work_md)
ax[0].plot(workSamples, work_hi)
ax[0].set_title("Work Load (#hrs)")

ax[1].plot(dateSamples, date_far)
ax[1].plot(dateSamples, date_close)
ax[1].set_title("Due Date (#days)")
#plt.savefig('nonClassMF03')
plt.show()

plt.plot(stressSamples, stress_lo)
plt.plot(stressSamples, stress_md)
plt.plot(stressSamples, stress_hi)
plt.axis(xmin=0, xmax=10)
plt.title("Stress Level")
#plt.savefig('nonClassConsMF')
plt.show()

# get activated membership functions
workload = 5
work_loTest = memberVal(workSamples, work_lo, workload)
work_mdTest = memberVal(workSamples, work_md, workload)
work_hiTest = memberVal(workSamples, work_hi, workload)

duedate = 12
date_close = memberVal(dateSamples, date_close, duedate)
date_far = memberVal(dateSamples, date_far, duedate)

#if workload lo then stress lo
rule1 = corrMin([work_loTest, stress_lo])
#if workload md and due dates far then md
rule2 = corrMin([ANDop([work_mdTest, date_far]), stress_md])
#if workload hi and due dates close then stress high
rule3 = corrMin([ANDop([work_hiTest, date_close]), stress_hi])

aggregated = aggregate([rule1, rule2, rule3], "max")
result = centroidDefuzz(stressSamples, aggregated)

# graph resultant graph with aggreagation and centroid
plt.plot(stressSamples, stress_lo)
plt.plot(stressSamples, stress_md)
plt.plot(stressSamples, stress_hi)
plt.fill_between(stressSamples, aggregated, alpha=0.4, color="b")
plt.axvline(result, color="b")
plt.axis(xmin=0, xmax=10)
plt.title('Aggregated and Defuzzified')
#plt.savefig('nonClassConsGraph2012')
plt.show()

print(result)