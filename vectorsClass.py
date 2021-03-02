"""
This code is to develop and create vector notations as a class for use in Rhinoscript space.
Vers. 1.1:
    Takes existing vector class development and transform it to a smaller profile as
    a class definition

Developed by Robostrike
Started on March 1, 2021
"""


import rhinoscriptsyntax as rs
import operator as op
import math as ma

class vec():
    
    
    
    def ptCheck(self,a):
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
    
    #dot product
    def dot(self,a,b):
        
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
    
    def dist(self,a,b):
        
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return ma.sqrt((b[0]-a[0])*(b[0]-a[0]) + (b[1]-a[1])*(b[1]-a[1]) + (b[2]-a[2])*(b[2]-a[2]))
    
    def vecDist(self,a):
        #distance of point to origin
        a = self.ptCheck(a)
        
        return ma.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
    
    
    def vecAdd(self,a,b):
        #add two vectors
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (a[0]+b[0],a[1]+b[1],a[2]+b[2])
    
    
    def vecSub(self,a,b):
        #subtract two vectors a --> b
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return (b[0]-a[0],b[1]-a[1],b[2]-a[2])
    
    
    def vecMult(self,a,b):
        #multiply one vector by a constant value 'b'
        a = self.ptCheck(a)
        
        return (a[0]*b,a[1]*b,a[2]*b)
    
    def vecCross(self,a,b):
        #cross product of two variables
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        c = (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-a[1]*b[0])
        
        return c
    
    
    def vecUnit(self,a):
        #unit vector of one variable
        a = self.ptCheck(a)
        b = self.dist(a,(0,0,0))
        
        #check distance and if it is 0, will create divide by 0 situation.
        if b < 0.0001:
            print "Attempt at dividing by 0"
            exit()
        else:
            return (a[0]/b , a[1]/b , a[2]/b)
    
    
    def vecAddUnit(self,a,b):
        return self.vecUnit(self.vecAdd(a,b))
    def vecSubUnit(self,a,b):
        return self.vecUnit(self.vecSub(a,b))
    def vecCrossUnit(self,a,b):
        return self.vecUnit(self.vecCross(a,b))
    
    def midPoint(self,a,b):
        a = self.ptCheck(a)
        b = self.ptCheck(b)
        
        return ((a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2)
    
    
    def ptLine(self,pt, lnPt1,lnPt2):
        #point and domain value of closest point along straight line
        
        #pt references existing point reference
        #lnPt1 denotes the starting point of the line
        #lnPt2 denotes the ending point of the line
        
        pt = self.ptCheck(pt)
        lnPt1 = self.ptCheck(lnPt1)
        lnPt2 = self.ptCheck(lnPt2)
        
        if self.dist(lnPt1,lnPt2) < 0.00005:
            print "Two Points of line are both same value, cannot compute"
            print lnPt1,lnPt2
            exit()
        
        
        #determine point position
        v1 = self.vecSubUnit(lnPt1,lnPt2)
        qx = lnPt1[0] - pt[0]
        qy = lnPt1[1] - pt[1]
        qz = lnPt1[2] - pt[2]
        
        top = qx*v1[0] + qy*v1[1] + qz*v1[2]
        bot = v1[0]*v1[0] + v1[1]*v1[1] + v1[2]*v1[2]
        
        division = top / bot
        position = self.vecAdd(lnPt1, vecMult(v1,-division))
        
        #determine from domain of from lnPt1.
        #0 is closest to lnPt1, 1 is closest to lnPt2
        v2 = self.vecSubUnit(lnPt1, position)
        lnPtDist = self.dist(lnPt1,lnPt2)
        ptDist = self.dist(lnPt1, position)
        quotient = self.vecDot(self.vecUnit(v2),self.vecUnit(v1))*ptDist/lnPtDist
        
        #returns the position, and domain value
        return (position,quotient)
    
    def linDiv (self,eq, eq2, set):
        #linear equation division
        value = eq[set]/eq2[set]
        return [eq[i] - eq2[i]*value for i in range(len(eq))]
    
    def linSub (self,eq, eq2):
        #linear equation subtraction
        return [eq[i] - eq2[i] for i in range(len(eq))]
    
    def ptPlane(self,plane, pt):
        #point closest plane value
        
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
        return self.vecAdd(pt, self.vecMult(plane[3],-lamb))


"""
#Testing Grounds
#initalize vectors sequencing
v = vec()
print v.midPoint((-9,2,3),(1,2,7))
"""