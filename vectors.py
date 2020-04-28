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
    #determines if the submitted point is a point object in space or array value
    #if object is 
    
    #designation implemented to determine if it is not a point object
    designation = 0
    
    try:
        if rs.ObjectType(a) == 1: #collect point object value
            b = rs.coerce3dpoint(a)
        elif rs.ObjectType(a)!= 1: #item is not a point
            designation = 1
    except:
        #item already an array object for use
        b = a
    
    #exporting value
    if designation == 0:
        return b
    #not a point object
    else:
        rs.UnselectAllObjects()
        print "Collecting point value but is another object type"
        rs.SelectObject(a)
        exit()

#dot product of two vectors
def vecDot(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#distance between two points
def dist(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))

#distance of point to origin
def vecDist(a):
    a = ptCheck(a)
    
    return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])

#add two vectors
def vecAdd(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

#subtract two vectors a --> b
def vecSub(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])

#multiply one vector by a constant value 'b'
def vecMult(a,b):
    a = ptCheck(a)
    
    return (a[0]*b,a[1]*b,a[2]*b)

#cross product of two variables
def vecCross(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    c = (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-a[1]*b[0])
    
    return c

#unit vector of one variable
def vecUnit(a):
    a = ptCheck(a)
    b = dist(a,(0,0,0))
    
    #check distance and if it is 0, will create divide by 0 situation.
    if b < 0.0001:
        print "Attempt at dividing by 0"
        exit()
    else:
        return (a[0]/b , a[1]/b , a[2]/b)


def vecAddUnit(a,b):
    return vecUnit(vecAdd(a,b))
def vecSubUnit(a,b):
    return vecUnit(vecSub(a,b))
def vecCrossUnit(a,b):
    return vecUnit(vecCross(a,b))

def midPoint(a,b):
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2)

#point closest along line
def pLineInt(pt, lnPt1,lnPt2):
    v1 = vecSubUnit(lnPt1,lnPt2)
    qx = lnPt1[0] - pt[0]
    qy = lnPt1[1] - pt[1]
    qz = lnPt1[2] - pt[2]
    
    top = qx*v1[0] + qy*v1[1] + qz*v1[2]
    bot = v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2]
    
    division = top / bottom
    
    return vecAdd(lnPt1, vecMult(v1,-division))

#point in relationship to the line in question
#(0,1) is within, and <0 is beyond start point, >1 is beyond the end point
def pLineIn(pt, lnPt1,lnPt2):
    v1 = vecSub(lnPt1, lnPt2)
    val = []
    for i in range(3):
        if v1[i]!= 0:
            #determine value relative from x/y/z perspective
            val.append((lnPt1[i] - pt[i]/v1[i])
    
    #assume it's the same value because it should be
    counter = 1
    for i in range(len(val)):
        for j in range(len(val)):
            if i!=j:
                if val[i] != val[j]:
                    counter == 0
    
    if counter == 1:
        quotient = val[0]
    else:
        quotient = -1000
        print "Error, point could not represent a value along line"
        exit()
    del val
    
    return quotient

#solve linear algebra to determine point on plane
#linear equation division
def linDiv (eq, eq2, set):
    value = eq[set]/eq2[set]
    return [eq[i] - eq2[i]*value for i in range(len(eq))]
#linear equation subtraction
def linSub (eq, eq2):
    return [eq[i] - eq2[i] for in range(len(eq))]
#point closest plane value
#plane is systematic of rhinoscript plane
def pPlane(plane, pt):


pt1 = (0,0,0)
pt2 = (2,0,0)
print midPoint(pt1,pt2)