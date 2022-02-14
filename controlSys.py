"""
This code is to develop control varaibles within the Rhinoscript space.
Vers. 1.0:
    Layer Manipulation and operations

Developed by Robostrike
Started on May 17, 2020

"""

import rhinoscriptsyntax as rs
import Rhino as r
import scriptcontext as sc
import operator as op
import math as ma
import os

def layerSet(text,color):
    #deletes existing information regarding this layer
    if rs.LayerId(text):
        rs.DeleteObjects(rs.ObjectsByLayer(text))
        rs.PurgeLayer(text)
    
    #recomputes layer as new layer
    rs.AddLayer(text,color)

def sorting(array1, listVal):
    #sorts the list of items in array1 based on the evaluated fitness value of
    #listVal. listVal will be sorted to lowest first incrementing to highest
    
    #returns the sorted list of objects
    
    temp = []
    temp2 = []
    
    #repeat the list for reference later
    for i in range(len(listVal)):
        temp.append(listVal[i])
    
    listVal.sort()
    
    for i in range(len(listVal)):
        temp2.append(array1[temp.index(listVal[i])])
    
    return temp2

def lay2pdf (name):
    #creates pdf based on rhino layout
    
    #initiate with
    """
    for i in sc.doc.Views:
        if type(i) is r.Display.RhinoPageView:
            lay2pdf(name)
    """
    
    
    filefolder = "C:\robostrike"
    if not (os.path.exists(filefolder)):
        os.makedirs(filefolder)
    
    pdf = r.FileIO.FilePdf.Create()
    dpi = 300
    width = 11
    height = 8.5
    size = System.Drawing.Size(width*dpi,height*dpi)
    settings = r.Display.ViewCaptureSettings(sc.docs.Views.ActiveView,size,dpi)
    
    extension = filefolder + "\\" +  name + ".pdf"
    
    pdf.AddPage(settings)
    pdf.Write(extension)
    