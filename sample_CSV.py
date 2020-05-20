import rhinoscriptsyntax as rs
import operator as op
import math as ma
import csv
import os

#create filepath to store your information
filepath = "C:\\CSV"

#check if the filepath exists on your computer
if not os.path.exists(filepath):
    #generates filepath if not exist
    os.makedirs(filepath)

