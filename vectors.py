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
    
    designation = 0
    
    try:
        if rs.ObjectType(a) == 1: #collect point object value
            b = rs.coerce3dpoint(a)
        elif rs.ObjectType(a)!= 1: #item is not a point
            designation = 1
    except:
        #item already an array object for use
        b = a
    
    if designation == 0:
        return b
    else:
        rs.UnselectAllObjects()
        print "Collecting point value but is another object type"
        rs.SelectObject(a)
        exit()

def dot(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def dist(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))

def vecDist(a):
    a = ptCheck(a)
    
    return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])

def vecAdd(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def vecSub(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])





pt1 = (0,0,0)
pt2 = (2,0,0)
print dist(pt1,pt2)