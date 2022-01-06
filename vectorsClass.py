"""
This code is to develop and create vector notations as a class for use in Rhinoscript space.
Vers. 1.1:
    Takes existing vector class development and transform it to a smaller profile as
    a class definition
Vers. 1.2:
    To complete still: do all case study test to ensure it works because transfers may
    cause bugs
Vers. 1.3:
    Added a ton of comments to speed up function call designations and clean up code

Developed by Robostrike
Started on March 1, 2021

"""


import rhinoscriptsyntax as rs
import operator as op
import math as ma

class vec():
    
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
    
    """
    
    
    def ptCheck(self,a):
        #determines if the submitted point or vector is valid
        #(x value, y value, z value)
        
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
    
    def planeCheck(self,a):
        #determines if the submitted plane is a plane object
        #(origin, x axis, y axis, z axis)
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
    
    #dot product
    def dot(self,a,b):
        """Computes the dot product of two vectors
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          number: overlap amount between first vector to second vector
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.dot(point1,point2)
        """
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
    
    def dist(self,a,b):
        """Computes the distance between points
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          number: scalar magnitude between two points
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.dist(point1,point2)
        """
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))
    
    def vecDist(self,a):
        """Computes the scalar magnitude of the intended vector
        Parameters:
          point1: point 3d or referenced point
        Returns:
          number: scalar magnitude of the vector
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.vecDist(point1)
        """
        a = self.ptCheck(a)
        
        return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
    
    
    def add(self,a,b):
        """Adds two vectors together
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.add(point1,point2)
        """
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
    
    
    def sub(self,a,b):
        """Subtracts two vectors a-->b
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.sub(point1,point2)
        """
        
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (b[0]-a[0],b[1]-a[1],b[2]-a[2])
    
    
    def mult(self,a,b):
        """Multiplies a vector to scalar magnitude
        Parameters:
          point1: point 3d or referenced point
          number: float value
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          value = 3
          v.mult(point1,value)
        """
        
        a = self.ptCheck(a)
        
        return (a[0]*b,a[1]*b,a[2]*b)
    
    def cross(self,a,b):
        """Computes the cross product of two vectors
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.cross(point1,point2)
        """
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        c = (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-a[1]*b[0])
        
        return c
    
    
    def vecUnit(self,a):
        """Unitizes the vector
        Parameters:
          point1: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          v.vecUnit(point1)
        """
        a = self.ptCheck(a)
        b = self.dist(a,(0,0,0))
        
        #check distance and if it is 0, will create divide by 0 situation.
        if b < 0.0001:
            print "Attempt at dividing by 0"
            exit()
        else:
            return (a[0]/b , a[1]/b , a[2]/b)
    
    
    def addUnit(self,a,b):
        """Adds two vectors together and then unitize it
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.addUnit(point1,point2)
        """
        return self.vecUnit(self.add(a,b))
    def subUnit(self,a,b):
        """Subtracts two vectors a-->b and then unit vectorize
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.subUnit(point1,point2)
        """
        return self.vecUnit(self.sub(a,b))
    def crossUnit(self,a,b):
        """Computes the unit vector of a two vector cross product
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.crossUnit(point1,point2)
        """
        return self.vecUnit(self.cross(a,b))
    
    def midPt(self,a,b):
        """Computes the unit vector of a two vector cross product
        Parameters:
          point1: point 3d or referenced point
          point2: point 3d or referenced point
        Returns:
          point: point 3d
        Example:
          v = vec()
          point1 = (1,2,3)
          point2 = (-2,1,3)
          v.midPt(point1,point2)
        """
        
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return ((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2)
    
    
    def massVA(self,set):
        """Adds all the point values together
        Parameters:
          point array: [point1, point2, ...]
        Returns:
          point: point 3d
        Example:
          v = vec()
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
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return self.add(a,self.mult(b,c))
    
    
    def ptLn(self,pt, lnPt1,lnPt2):
        """Computes a point closest to a line
        Parameters:
          point1: evaluating point 3d or referenced point
          point2: point 3d or referenced point of a line
          point3: point 3d or referenced point of a line at another position
        Returns:
          point[0]: point 3d that will be on or closest to the line
          value[1]: scalar magnitude distance from point2 along vector point2 --> point3
        Example:
          v = vec()
          point1 = (1,2,3)
          line1 = (-2,1,3)
          line2 = (10,3,4)
          v.ptLn(point1,line1,line2)
        """
        
        pt = self.ptCheck(pt)
        lnPt1 = self.ptCheck(lnPt1)
        lnPt2 = self.ptCheck(lnPt2)
        
        if self.dist(lnPt1,lnPt2) < 0.00005:
            print "Two Points of line are both same value, cannot compute"
            print lnPt1,lnPt2
            exit()
        
        
        #determine point position
        v1 = self.subUnit(lnPt1,lnPt2)
        qx = lnPt1[0] - pt[0]
        qy = lnPt1[1] - pt[1]
        qz = lnPt1[2] - pt[2]
        
        top = qx*v1[0] + qy*v1[1] + qz*v1[2]
        bot = v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2]
        
        division = top / bot
        position = self.add(lnPt1, self.mult(v1,-division))
        
        #determine from domain of from lnPt1.
        #0 is closest to lnPt1, 1 is closest to lnPt2
        v2 = self.sub(lnPt1, position)
        lnPtDist = self.dist(lnPt1,lnPt2)
        ptDist = self.dist(lnPt1, position)
        if op.abs(self.vecDist(v2)) < 0.001:
            return (position, 0)
        else:
            quotient = self.dot(self.vecUnit(v2),self.vecUnit(v1))*ptDist/lnPtDist
            
            #returns the position, and domain value
            return (position,quotient)
    
    def linDiv (self,eq, eq2, set):
        #linear equation division
        
        value = eq[set]/eq2[set]
        return [eq[i] - eq2[i]*value for i in range(len(eq))]
    
    def linSub (self,eq, eq2):
        #linear equation subtraction
        return [eq[i] - eq2[i] for i in range(len(eq))]
    
    def ptPl(self,plane, pt):
        """Computes a point closest to the plane (perpendicular)
        Parameters:
          plane: prescribed plane of origin, and xyz axis
          point: point 3d or referenced point for evaluation
        Returns:
          point: point 3d that will be on or closest to the line
        Example:
          import rhinoscriptsyntax as rs
          v = vec()
          plane = rs.PlaneFromPoints((0,0,0),(10,4,5),(-1,4,2))
          point = (-5,-3,5)
          v.ptPl(plane,pt)
        """
        
        
        pt = self.ptCheck(pt)
        plane = self.planeCheck(plane)
        
        px=  [plane[1][0],plane[2][0],plane[3][0], pt[0]-plane[0][0]]
        py = [plane[1][1],plane[2][1],plane[3][1], pt[1]-plane[0][1]]
        pz = [plane[1][2],plane[2][2],plane[3][2], pt[2]-plane[0][2]]
        
        #value preset if first set is 0
        pXY = py
        pXZ = pz
        
        if plane[1][1] != 0:
            pXY = self.linDiv(px,py,0)
        if plane[1][2] != 0:
            pXZ = self.linDiv(px,pz,0)
        
        pYZ = self.linSub(pXY,pXZ)
        
        if pXZ[1]!= 0:
            pYZ = self.linDiv(pXY,pXZ,1)
        
        lamb = pYZ[3]/pYZ[2]
        return self.add(pt, self.mult(plane[3],-lamb))
    
    
    def matrixAdd(self,a,b):
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
        
    def matrixMultConst(self,a,b):
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
    
    def lnLn(self,ptA1,ptA2,ptB1,ptB2):
        """Computes a line to line closest or intersection operation
        Parameters:
          line1A: point 3d or referenced point of line 1
          line1B: point 3d or referenced point of line 1
          line2A: point 3d or referenced point of line 2
          line2B: point 3d or referenced point of line 2
        Returns:
          number[0]: type of intersection value
            1 - lie on same line
            2 - parallel
            3 - non parallel but do not intersect
            4 - non parallel and intersect at one point
          point[1]: point on line 1 closest to line 2
          parameter[2]: parameter in vector of line1A to line1B to point[1]
          point[3]: point on line 2 closest to line 1
          parameter[4]: parameter in vector of line2A to line2B to point[3]
          number[5]: distance between point[1] and point[3]
        Example:
          v = vec()
          line1A = (-2,1,3)
          line1B = (10,3,4)
          line2A = (2,2,4)
          line2B = (7,2,-1)
          v.lnLn(line1A,line1B,line2A,line2B)
        """
        
        
        
        ptA1 = self.ptCheck(ptA1)
        ptA2 = self.ptCheck(ptA2)
        ptB1 = self.ptCheck(ptB1)
        ptB2 = self.ptCheck(ptB2)
        
        
        #determines the position of nearest point connection and type (identifier)
        #1 = colinear and both lines are parallel and together
        #2 = colinear and both lines are equidistant apart
        #3 = closest point but not touching
        #4 = intersection at one point
        
        
        
        #separate 12 with 34 by checking their vectors
        
        v1 = self.sub(ptA1,ptA2)
        v2 = self.sub(ptB1,ptB2)
        
        v1Unit = self.vecUnit(v1)
        v2Unit = self.vecUnit(v2)
        
        
        v12Dot = self.dot(v1Unit,v2Unit)
        
        #determines colinearity by dot product = 1 (as either -1 or 1)
        if op.abs(v12Dot) > .999:
            #check if it is a type 1 and if two of its values are the same
            pointRef = self.ptLine(ptA1,ptB1,ptB2)
            if self.dist(pointRef[0],ptA1) < 0.0005:
                return (1,ptA1,0,ptB1,0,0)
            else:
                return (2,ptA1,0,ptB1,0,self.dist(ptA1,pointRef[0]))
            
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
                oB = self.matrixMultConst(oA,v1[i])
                oC = self.matrixMultConst(oA,v2[i])
                
                o1 = self.matrixAdd(o1,oB)
                o2 = self.matrixAdd(o2,oC)
                
                del oA
                del oB
                del oC
                
            
            #system of equations to resolve for s and t values
            if (o1[0] == 0) & (o1[1] == 0):
                #unsolveable equation
                print "Cannot compute line line intersection value due to indetermined condition"
                exit()
            else:
                #solve linear algebra and isolate for t
                o3 = self.matrixMultConst(o2,0-o1[0]/o2[0])
                o4 = self.matrixAdd(o3,o1)
                
                st[1] = 0-o4[2]/o4[1]
                
                if o1[0] == 0:
                    
                    st[0] = (0-o2[2]-st[1]*o2[1])/o2[0]
                else:
                    
                    st[0] = (0-o1[2]-st[1]*o1[1])/o1[0]
            
            #now that you know what the values of s and t are. Substitute it back
            #into the original equation.
            
            ptAf = self.add(ptA1,self.mult(v1,st[1]))
            ptBf = self.add(ptB1,self.mult(v2,st[0]))
            
            distance = self.dist(ptAf,ptBf)
            if distance > 0.0005:
                #type 3
                return (3,ptAf,st[1],ptBf,st[0],distance)
            else:
                #type 4
                return (4,ptAf,st[1],ptBf,st[0],distance)
    
    
    def lnPl (self,plane, ptA1, ptA2):
        """Computes the line and plane intersection
        Parameters:
          plane: prescribed plane of origin, and xyz axis
          line1A: point 3d or referenced point of line 1
          line1B: point 3d or referenced point of another point in line 1
        Returns:
          number[0]: type condition of intersection type
            1 - line is on plane and returns the designated line1A
            2 - unique solution
          point[1]: point 3d of intersection on plane
          parameter[2]: vector along line1A to line1B to reach intersection point
        Example:
          import rhinoscriptsyntax as rs
          v = vec()
          plane = rs.PlaneFromPoints((0,0,0),(10,4,5),(-1,4,2))
          line1A = (-5,-3,5)
          line1B = (10,5,1)
          v.lnPl(plane,line1A,line1B)
        """
        
        
        #determines the intersection point, or identify its parallelism
        
        ptA1 = self.ptCheck(ptA1)
        ptA2 = self.ptCheck(ptA2)
        
        plane = self.planeCheck(plane)
        
        #vector geometry calculation
        if self.dist(ptA1,ptA2) < 0.001:
            print ("Cannot compute plane line intersection value due to indetermined condition")
            exit()
        
        vecA = self.sub(ptA2,ptA1)  #vectorA
        pDist = self.sub(ptA1,plane[0])  #distance between static point of plane and line
        den = self.dot(self.mult(vecA,-1), plane[3])
        
        if op.abs(den) < 0.001:
            print "No unique solution"
            return (1, ptA1,0)
        
        crossU = self.cross(plane[2],self.mult(vecA,-1))
        crossV = self.cross(self.mult(vecA,-1),plane[1])
        
        t = self.dot(plane[3],pDist) / den
        u = self.dot(crossU,pDist) / den
        v = self.dot(crossV,pDist) / den
        
        pointF = self.add(ptA1,self.mult(vecA,-t))
        return (2,pointF,t)
    
    
    def plPl(self,plane1,plane2):
        """Computes the plane and plane intersection
        Parameters:
          plane1: prescribed plane of origin, and xyz axis
          plane2: prescribed plane of origin, and xyz axis
        Returns:
          number[0]: type condition of intersection type
            1 - plane is parallel to one another
            2 - plane is not parallel 
          point[1]: point 3d of an intersection position between two planes
          point[2]: point 3d of the vector of the line
        Example:
          import rhinoscriptsyntax as rs
          v = vec()
          plane1 = rs.PlaneFromPoints((0,0,0),(10,4,5),(-1,4,2))
          plane2 = rs.PlaneFromPoints((1,4,9),(3,12,9),(1,-2,1))
          v.plPl(plane1,plane2)
        """
        
        plane1 = self.planeCheck(plane1)
        plane2 = self.planeCheck(plane2)
        
        #determine if the two planes are parallel
        
        dotVal = self.dot(plane1[3],plane2[3])
        if (dotVal > 0.999) | (dotVal < -0.999):
            #parallel plane
            return (1,plane1[0],None)
        else:
            #get vector of interest
            vecOut = self.crossUnit(plane1[3],plane2[3])
            vecPerp = self.crossUnit(vecOut, plane1[3])
            point = v.lnPl(plane2,plane1[0],self.add(plane1[0],vecPerp))[1]
            
            return (2,point,vecOut)
    
    def pl3(self,plane1,plane2,plane3):
        """Computes the plane plane plane intersection
        Parameters:
          plane1: prescribed plane of origin, and xyz axis
          plane2: prescribed plane of origin, and xyz axis
          plane3: prescribed plane of origin, and xyz axis
        Returns:
          number[0]: type condition of intersection type
            1 - all 3 planes are parallel
            2 - 2 planes are parallel and one intersects
            3 - a unique solution of one point
          point[1]: point 3d of intersection if present
        Example:
          import rhinoscriptsyntax as rs
          v = vec()
          plane1 = rs.PlaneFromPoints((0,0,0),(10,4,5),(-1,4,2))
          plane2 = rs.PlaneFromPoints((1,4,9),(3,12,9),(1,-2,1))
          plane3 = rs.PlaneFromPoints((10,4,5),(3,5,-1),(-1,-5,10))
          v.pl3(plane1,plane2,plane3)
        """
        
        plane1 = self.planeCheck(plane1)
        plane2 = self.planeCheck(plane2)
        plane3 = self.planeCheck(plane3)
        
        #check for plane parallelism
        check1 = self.dot(plane1[3],plane2[3])
        check2 = self.dot(plane1[3],plane3[3])
        check3 = self.dot(plane2[3],plane3[3])
        
        
        
        
        
        
