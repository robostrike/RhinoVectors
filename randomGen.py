"""
This code is to develop and create a random variable assessibility for use in Rhinoscript space.
Vers. 1.0:
    Uses Linear Congruential Generator to compute the random values (and control them)
    Map function to remap domains for random values

Developed by Robostrike
Started on April 28, 2020

"""

import math as ma
import operator as op

class randVal:
    ct = 1013904223
    xn = 0
    a1 = 1664525
    mn = ma.pow(2,32)
    
    def __init__(self, seed,val):
        #creates a call stack of an initial value and the scope of value (from 0 to val)
        #eg. rand = randVal(12,23) to initiate an initial random value of 12 with the array stack going up to 23 values.
        self.x1 = seed
        self.mo = val
    
    def value(self):
        #returns the domain value of the random class object
        return self.mo
    
    def next(self):
        #generates the next value output
        #eg. rand.next() --> will generate the next tabled value
        self.xn = (self.a1*self.x1 + self.ct)%self.mn
        self.x1 = self.xn
        
        return int(self.xn%self.mo)

def map(domain,rand):
    #domain is the range from 0 to domain that the map will correlate to
    #rand is the class object of randVal used in the formation of domain
    
    next = rand.next()
    limit = rand.value()
    
    
    return domain*next/limit
