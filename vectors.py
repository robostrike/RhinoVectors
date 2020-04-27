"""
This code is to develop and create vector notations for use in Rhinoscript space.
Vers. 1.1:
    look into merging with other libraries to not lose the autofiller for syntax on other
    scripts. Right now having this imported for use on other scripts loses the ability
    for autocomplete to pop out when referencing this script.

Developed by Robostrike
Started on April 27, 2020
"""


import rhinoscriptsyntax as rs
import operator as op
import math as ma

def ptCheck(a):
    #determines if the submitted point is a point object in space or 
    #is an array value
    #or other
    
    """
    is a an array or data object identifier
    if a is array, return a
    if a is object identifier, determine its type
            if type is 1, get teh array value
            if type is not 1, then exit as it doesn't work and highlight it.
    
    """
    
    try:
        b = rs.coerce3dpoint(a)
    except:
        b = a
        
    return b

def dot(a,b):
    
    a = ptCheck(a)
    b = ptCheck(b)
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    


#how do you identify objects from an id to an actual set of 3 coordinate values

#split between it being a 

pt1 = rs.ObjectsByLayer("Default")[0]
#so if there's only  one object, it's defined within each item... so the [] array parameter inside another array is what's causing the 'none' results to occur.
#lists have to be idnividually handled

pt2 = (0,0,10)

print dot(pt1,pt2)

#parser for information