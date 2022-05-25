"""
This code is to develop and create vector notations for use in Rhinoscript space.
Vers. 1.1:
    look into merging with other libraries to not lose the autofiller for syntax on other
    scripts. Right now having this imported for use on other scripts loses the ability
    for autocomplete to pop out when referencing this script.

Vers. 1.2:
    Includes matrix manipulation to deal with line line connection

Vers. 1.3:
    Includes plane and line intersection

Developed by Robostrike
Started on April 27, 2020
"""


import rhinoscriptsyntax as rs
import operator as op
import math as ma

"""
    Initiate with v = vec()
    
    
    Command List:
    
    CHECKS
    ptCheck     Checks for validity of point for usage
    planeCheck  Checks for validity of plane for usage
    
    VECTORS
    dot         Computes dot product of two vectors
    dist        Computes the distance between two points
    vecDist     Computes the scalar magnitude of the vector
    add         Adds two vectors together
    sub         Subtracts the first to the second vector 1-->2
    mult        Multplies a vector to a scalar value
    cross       Computes the cross product of two vectors
    vecUnit     Reproduces the vector to scalar magnitude of 1
    addUnit     Adds two vectors together and change the scalar magnitude to 1
    subUnit     Subtracts two vectors and changes the scalar magnitude to 1
    crossUnit   Computes cross multiplication and scale to magnitude of 1
    midPt       Computes the mid point value of two points
    massVA      Computes the addition of all point and vector values of a (set)
    addMult     Adds the first vector to a scalar multiplication of another vector
    
    EQUATION SYSTEMS
    ptLn        Computes the point closest to a line (point, value)
    ptPl        Computes the point closest to a plane
    lnLn        Computes the line closest to line intersection
    lnPl        Computes the line to a plane intersection
    plPl        Computes the plane to a plane vector intersection
    pl3         Computes the plane plane plane intersection
    """


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


def dot(a,b):
    """Computes the dot product of two vectors
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          number: overlap amount between first vector to second vector
        Example:
          import vectors as v
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.dot(point1,point2)
        """
    a = ptCheck(a)
    b = ptCheck(b)
    
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def dist(a,b):
    """Computes the distance between points
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          number: scalar magnitude between two points
        Example:
          import vectors as v
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.dist(point1,point2)
        """
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))


def vecDist(a):
    """Computes the scalar magnitude of the intended vector
        Parameters:
          point1: point 3d or referenced point
        Returns:
          number: scalar magnitude of the vector
        Example:
          import vectors as v
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.vecDist(point1)
        """
    a = ptCheck(a)
    
    return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])


def add(a,b):
    """Adds two vectors together
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          import vectors as v
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.add(point1,point2)
        """
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])


def sub(a,b):
    """Subtracts two vectors a-->b
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.sub(point1,point2)
    """
    a = ptCheck(a)
    b = ptCheck(b)
    
    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])


def mult(a,b):
    """Multiplies a vector to scalar magnitude
    Parameters:
      point1: point 3d or referenced point
      number: float value
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      value = 3
      v.mult(point1,value)
    """
    a = ptCheck(a)
    
    return (a[0]*b,a[1]*b,a[2]*b)

def cross(a,b):
    """Computes the cross product of two vectors
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.cross(point1,point2)
    """
    a = ptCheck(a)
    b = ptCheck(b)
    
    c = (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-a[1]*b[0])
    
    return c


def vecUnit(a):
    """Unitizes the vector
    Parameters:
      point1: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      v.vecUnit(point1)
    """
    a = ptCheck(a)
    b = dist(a,(0,0,0))
    
    #check distance and if it is 0, will create divide by 0 situation.
    if b < 0.0001:
        print "Attempt at dividing by 0"
        exit()
    else:
        return (a[0]/b , a[1]/b , a[2]/b)


def addUnit(a,b):
    """Adds two vectors together and then unitize it
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.addUnit(point1,point2)
    """
    return vecUnit(vecAdd(a,b))
def subUnit(a,b):
    """
    Subtracts two vectors a-->b and then unit vectorize
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.subUnit(point1,point2)
    """
    return vecUnit(vecSub(a,b))
def crossUnit(a,b):
    """
    Computes the unit vector of a two vector cross product
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.crossUnit(point1,point2)
    """
    return vecUnit(cross(a,b))

def midPt(a,b):
    """Computes the unit vector of a two vector cross product
    Parameters:
      point1: point 3d or referenced point
      point2: point 3d or referenced point
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      v.midPt(point1,point2)
    """
    a = ptCheck(a)
    b = ptCheck(b)
    
    return ((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2)

def massVA(set):
    """Adds all the point values together
    Parameters:
      point array: [point1, point2, ...]
    Returns:
      point: point 3d
    Example:
      import vectors as v
      point1 = (1,2,3)
      point2 = (-2,1,3)
      point3 = (10,3,5)
      v.massVA((point1,point2,point3))
    """
    
    ptSet = (0,0,0)
    for i in range(len(set)):
        ptSet = self.add(ptSet,set[i])
    return ptSet

def addMult(self,a,b,c):
    """Adds one point / vector to another multiplied by a scalar value
    Parameters:
      point1: point 3d or referenced 3d point
      point2: point 3d or referenced 3d point
      number: a scalar value for point 2
    Returns:
      point: point 3d
    Example:
      v = vec()
      point1 = (1,2,3)
      point2 = (-2,1,3)
      value = 3
      v.addMult(point1,point2,value)
    """
    #a and b are vectors
    #c is a scalar value multiplied to vector b
    a = ptCheck(a)
    b = ptCheck(b)
    
    return add(a,mult(b,c))

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
    position = add(lnPt1, mult(v1,-division))
    
    #determine from domain of from lnPt1.
    #0 is closest to lnPt1, 1 is closest to lnPt2
    v2 = subUnit(lnPt1, position)
    lnPtDist = dist(lnPt1,lnPt2)
    ptDist = dist(lnPt1, position)
    quotient = dot(vecUnit(v2),vecUnit(v1))*ptDist/lnPtDist
    
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
    return addMult(pt,plane[3],-lamb)

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
    #returns the the type of connection, the point of each reference, and position
    #from ptA1 and ptB1, and distance if possible between each other
    #[type, intersection point A, val within A (0-1 is within), 
    #       intersection point B, val within B (0-1 is within, distance if parallel]
    
    
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
    
    v1 = sub(ptA1,ptA2)
    v2 = sub(ptB1,ptB2)
    
    v1Unit = vecUnit(v1)
    v2Unit = vecUnit(v2)
    
    
    v12Dot = dot(v1Unit,v2Unit)
    
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
            
            st[1] = 0-o4[2]/o4[1]
            
            if o1[0] == 0:
                
                st[0] = (0-o2[2]-st[1]*o2[1])/o2[0]
            else:
                
                st[0] = (0-o1[2]-st[1]*o1[1])/o1[0]
        
        #now that you know what the values of s and t are. Substitute it back
        #into the original equation.
        
        ptAf = add(ptA1,mult(v1,st[1]))
        ptBf = add(ptB1,mult(v2,st[0]))
        
        distance = dist(ptAf,ptBf)
        if distance > 0.0005:
            #type 3
            return (3,ptAf,st[1],ptBf,st[0],distance)
        else:
            #type 4
            return (4,ptAf,st[1],ptBf,st[0],distance)


def planeln (plane, ptA1, ptA2):
    #determines the intersection point, or identify its parallelism
    
    ptA1 = ptCheck(ptA1)
    ptA2 = ptCheck(ptA2)
    
    plane = planeCheck(plane)
    
    #vector geometry calculation
    if dist(ptA1,ptA2) < 0.001:
        print ("Line distance too short")
        exit()
    
    vecA = sub(ptA2,ptA1)  #vectorA
    pDist = sub(ptA1,plane[0])  #distance between static point of plane and line
    den = dot(mult(vecA,-1), plane[3])
    
    if op.abs(den) < 0.001:
        print "No unique solution"
        return (1, "No Unique Solution")
    
    crossU = cross(plane[2],mult(vecA,-1))
    crossV = cross(mult(vecA,-1),plane[1])
    
    t = dot(plane[3],pDist) / den
    u = dot(crossU,pDist) / den
    v = dot(crossV,pDist) / den
    
    pointF = add(ptA1,mult(vecA,-t))
    return (0,t,pointF)