"""
This code is to develop a sample comma separated value for use in Rhinoscript
Vers. 1.0:
    writes a sample file onto the computer
    reads from the same file and stored in an array

Developed by Robostrike
Started on May 20, 2020

"""

import csv
import os


#create filepath to store your information
filepath = "C:\\CSV"
filename = "sampleCSV.csv"

#check if the filepath exists on your computer
if not os.path.exists(filepath):
    #generates filepath if not exist
    os.makedirs(filepath)

#opens a filepath with a filename
file = open(filepath+"\\" + filename, 'w')

#writes dedicated information
text = "1,new,3,x-2"
file.write(text + "\n")
file.write(text + "\n")

#always close the file to prevent the file from being read only still receiving
#input data
file.close()


#reading csv files is also necessary to do some basic search operations on
#mass information relays

#read data from file
with open(filepath + "\\" + filename, 'rb') as f:
    #reads information and separates items by new line and commas
    reader = csv.reader(f)
    #data object is created with stored value
    data = list(reader)

#print the data to show the result
print data