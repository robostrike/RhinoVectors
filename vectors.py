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



def dot(a,b):
    
    
    try:
        a = rs.coerce3dpoint(a)
    except:
        pass
    
    try:
        b = rs.coerce3dpoint(b)
    except:
        pass
    
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    


#how do you identify objects from an id to an actual set of 3 coordinate values

#split between it being a 

pt1 = rs.ObjectsByLayer("Default")



pt2 = (0,0,10)

#parser for information


print rs.ObjectType(pt1)

