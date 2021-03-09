#!/usr/bin/env python

import sys
import statistics

def reducer():
    sampleAggregation={}
    for line in sys.stdin:
        line=line.strip()
        #print(line)
        groupId_str,MemoryUtilization = line.split()
        groupId=int(groupId_str)
        if groupId not in sampleAggregation:
            sampleAggregation[groupId]=list()
            sampleAggregation[groupId].append(float(MemoryUtilization))
        else:
            sampleAggregation[groupId].append(float(MemoryUtilization))
           
    for key in sampleAggregation:
        listOfRange =sampleAggregation.get(key)
        minimum = min(listOfRange)
        maximum = max(listOfRange)
        average  = sum(listOfRange)/len(listOfRange)
        medianforList=statistics.median(listOfRange)
        standardDeviation=statistics.stdev(listOfRange)
        print("%s \t %s" % ('samples for group '+ str(key), len(listOfRange)))
        print("%s \t %s" % ('minimum for group '+ str(key), minimum))
        print("%s \t %s" % ('maximum for group '+ str(key), maximum))
        print("%s \t %s" % ('mean for group '+ str(key), average))
        print("%s \t %s" % ('median for group '+ str(key), medianforList))
        print("%s \t %s" % ('standard Deviation for group '+ str(key), standardDeviation))
        #emit minimum
        #emit maximum
        #emit mean
        #emit standarddeviation
reducer()
