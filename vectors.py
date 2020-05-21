"""
This code is to develop and create vector notations for use in Rhinoscript space.
Vers. 1.1:
    look into merging with other libraries to not lose the autofiller for syntax on other
    scripts. Right now having this imported for use on other scripts loses the ability
    for autocomplete to pop out when referencing this script.

Vers. 1.2:
    Includes matrix manipulation to deal with line line connection

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

def planeCheck(a):
    #determines if the submitted plane is a plane object
    #there's 4 point references (origin, x, y, z axis)
    count = 0
    try:
        for i in range(len(a)):
            #just checks to see if it's an object at this bin, of 4 items
            if len(a[i]) == 3:
                count = count + 1
    except:
        pass
    
    if count == 4:
        #valid item
        return a
    
    
    else:
        print "Invalid plane"
        print a
        exit()


def vecDot(a,b):
    #dot product of two vectors
    a = ptCheck(a)
    b = ptCheck(b)
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def dist(a,b):
    #distance between two points
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))


def vecDist(a):
    #distance of point to origin
    a = ptCheck(a)
    
    return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])


def vecAdd(a,b):
    #add two vectors
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])


def vecSub(a,b):
    #subtract two vectors a --> b
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])


def vecMult(a,b):
    #multiply one vector by a constant value 'b'
    a = ptCheck(a)
    
    return (a[0]*b,a[1]*b,a[2]*b)

def vecCross(a,b):
    #cross product of two variables
    a = ptCheck(a)
    b = ptCheck(b)
    
    c = (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-a[1]*b[0])
    
    return c


def vecUnit(a):
    #unit vector of one variable
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


def ptLine(pt, lnPt1,lnPt2):
    #point and domain value of closest point along straight line
    
    #pt references existing point reference
    #lnPt1 denotes the starting point of the line
    #lnPt2 denotes the ending point of the line
    
    pt = ptCheck(pt)
    lnPt1 = ptCheck(lnPt1)
    lnPt2 = ptCheck(lnPt2)
    
    if dist(lnPt1,lnPt2) < 0.00005:
        print "Two Points of line are both same value, cannot compute"
        print lnPt1,lnPt2
        exit()
    
    
    #determine point position
    v1 = vecSubUnit(lnPt1,lnPt2)
    qx = lnPt1[0] - pt[0]
    qy = lnPt1[1] - pt[1]
    qz = lnPt1[2] - pt[2]
    
    top = qx*v1[0] + qy*v1[1] + qz*v1[2]
    bot = v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2]
    
    division = top / bot
    position = vecAdd(lnPt1, vecMult(v1,-division))
    
    #determine from domain of from lnPt1.
    #0 is closest to lnPt1, 1 is closest to lnPt2
    v2 = vecSubUnit(lnPt1, position)
    lnPtDist = dist(lnPt1,lnPt2)
    ptDist = dist(lnPt1, position)
    quotient = vecDot(vecUnit(v2),vecUnit(v1))*ptDist/lnPtDist
    
    #returns the position, and domain value
    return (position,quotient)

#solve linear algebra to determine point on plane
def linDiv (eq, eq2, set):
    #linear equation division
    value = eq[set]/eq2[set]
    return [eq[i] - eq2[i]*value for i in range(len(eq))]

def linSub (eq, eq2):
    #linear equation subtraction
    return [eq[i] - eq2[i] for i in range(len(eq))]

def ptPlane(plane, pt):
    #point closest plane value
    
    pt = ptCheck(pt)
    plane = planeCheck(plane)
    
    px=  [plane[1][0],plane[2][0],plane[3][0], pt[0]-plane[0][0]]
    py = [plane[1][1],plane[2][1],plane[3][1], pt[1]-plane[0][1]]
    pz = [plane[1][2],plane[2][2],plane[3][2], pt[2]-plane[0][2]]
    
    #value preset if first set is 0
    pXY = py
    pXZ = pz
    
    if plane[1][1] != 0:
        pXY = linDiv(px,py,0)
    if plane[1][2] != 0:
        pXZ = linDiv(px,pz,0)
    
    pYZ = linSub(pXY,pXZ)
    
    if pXZ[1]!= 0:
        pYZ = linDiv(pXY,pXZ,1)
    
    lamb = pYZ[3]/pYZ[2]
    return vecAdd(pt, vecMult(plane[3],-lamb))

def matrixAdd(a,b):
    #matrix a and b are added together (must be same size)
    
    #checks for same size
    check = 0
    c = 1
    d = 1
    if len(a) == len(b):
        try:
            #float could be an int if a[0] only contains one value and is not an array
            c = len(a[0])
            d = len(b[0])
        except:
            pass
        
        if c == d:
            check = 1
    
    #if test passes and both are of same size
    if check == 1:
        #create empty array
        result = [[0 for i in range(c)]for j in range(len(a))]
        for i in range(len(a)):
            for j in range(c):
                if c == 1:
                    result[i] = a[i] + b[i]
                else:
                    result[i][j] = a[i][j] + b[i][j]
        return result
    else:
        #if matrix size is not the same
        print "matrix size is not the same"
        return None

def matrixMultConst(a,b):
    #matrix a multiplies by constant b
    
    #check column dimension
    c = 1
    try:
        #float could be an int if a[0] only contains one value and is not an array
        c = len(a[0])
    except:
        pass
    
    #create empty array
    result = [[0 for i in range(c)] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(c):
            if c == 1:
                result[i] = a[i]*b
            else:
                result[i][j] = a[i][j]*b
    
    return result

def lnln(ptA1,ptA2,ptB1,ptB2):
    #incomplete / inaccurate
    
    #returns the the type of connection, the point of each reference, and position
    #from ptA1 and ptB1, and distance if possible between each other
    
    ptA1 = ptCheck(ptA1)
    ptA2 = ptCheck(ptA2)
    ptB1 = ptCheck(ptB1)
    ptB2 = ptCheck(ptB2)
    
    
    #determines the position of nearest point connection and type (identifier)
    #1 = colinear and both lines are parallel and together
    #2 = colinear and both lines are equidistant apart
    #3 = closest point but not touching
    #4 = intersection at one point
    
    
    
    #separate 12 with 34 by checking their vectors
    
    v1 = vecSub(ptA1,ptA2)
    v2 = vecSub(ptB1,ptB2)
    
    v1Unit = vecUnit(v1)
    v2Unit = vecUnit(v2)
    
    
    v12Dot = vecDot(v1Unit,v2Unit)
    
    #determines colinearity by dot product = 1 (as either -1 or 1)
    if op.abs(v12Dot) == 1:
        #check if it is a type 1 and if two of its values are the same
        pointRef = ptLine(ptA1,ptB1,ptB2)
        if dist(pointRef[0],ptA1) < 0.0005:
            return (1,ptA1,0,ptB1,0,0)
        else:
            return (2,ptA1,0,ptB1,0,dist(ptA1,pointRef[0]))
        
        del pointRef
    else:
        #solve linear equation. If possible, then it's type 4, else, type 3.
        #v12 is vector from line 1 to line 2 closest value
        #[s,t,c] where s is for v1 to point of A, t is for v2 to point of B
        #c is constant
        o1 = [0,0,0]
        o2 = [0,0,0]
        st = [0,0,0]
        for i in range(len(ptA1)):
            oA = [v2[i],0-v1[i],ptB1[i]-ptA1[i]]
            oB = matrixMultConst(oA,v1[i])
            oC = matrixMultConst(oA,v2[i])
            
            o1 = matrixAdd(o1,oB)
            o2 = matrixAdd(o2,oC)
            
            del oA
            del oB
            del oC
            
        #system of equations to resolve for s and t values
        if (o1[0] == 0) & (o1[1] == 0):
            #unsolveable equation
            print "Cannot compute value due to cancelled terms"
            exit()
        else:
            #solve linear algebra and isolate for t
            o3 = matrixMultConst(o2,0-o1[0]/o2[0])
            o4 = matrixAdd(o3,o1)
            st[1] = o4[2]/o4[1]
            if o1[0] == 0:
                st[0] = (0-o2[2]-st[1]*o2[1])/o2[0]
            else:
                st[0] = (0-o1[2]-st[1]*o1[1])/o1[0]
        
        #now that you know what the values of s and t are. Substitute it back
        #into the original equation.
        
        ptAf = vecAdd(ptA1,vecMult(v1,st[0]))
        ptBf = vecAdd(ptB1,vecMult(v2,st[1]))
        
        distance = dist(ptAf,ptBf)
        if distance > 0.0005:
            #type 3
            return (3,ptAf,vecDist(v1)*st[0],ptBf,vecDist(v2)*st[1],distance)
        else:
            #type 4
            return (4,ptAf,vecDist(v1)*st[0],ptBf,vecDist(v2)*st[1],distance)

pt1 = (0,0,0)
pt2 = (10,0,0)
pt3 = (0, 5, 0)
pt4 = (5,0,0)

print lnln(pt1,pt2,pt3,pt4)
