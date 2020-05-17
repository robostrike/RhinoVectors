"""
This code is to develop control varaibles within the Rhinoscript space.
Vers. 1.0:
    Layer Manipulation and operations

Developed by Robostrike
Started on May 17, 2020

"""

import rhinoscriptsyntax as rs
import operator as op
import math as ma

def layerSet(text,color):
    #deletes existing information regarding this layer
    if rs.LayerId(text):
        rs.DeleteObjects(rs.ObjectsByLayer(text))
        rs.PurgeLayer(text)
    
    #recomputes layer as new layer
    rs.AddLayer(text,color)

