# RhinoVectors
A series of vector functions to assist with Rhinoscript



vectors.py

Incorporates linear algebra definitions for point utility

randomGen.py

A random number generator, varied by seed, to conduct controlled
random values.
There also includes a map function to tie within a certain scope
from 0 to alloted value in association to it.

GENERAL NOTES

Lessons learned having developed a coding practice at the Quicken Loans 
metal panel facade in 2018-2019 in the Rhino + Grasshopper + Pythonscript 
scene. Here are some key take aways:

- Build temporary layers to store completed objects and ones that will allow 
you to manipulate objects in before sending them into a separate more secure 
layer. This way repeating objects have a space for all its work before submitting
to a safe spot.
- Delete objects of the temporary layer once each action is completed. You can go
as far as deleting the layer itself, but as long as all objects of that layer are
gone, then you're ready to move onto the next object. Failure to do so will create
unnecessary duplicate actions which will probably fail the system or intended outcomes.
Also ensure to release used objects such as using (del variableName) so that the
information is not used as referenced for the next object build.
- Building objects should first check for existing references before building
over. Since scripts don't have their own feedback loop, you'll have to check
your own work. Checks can include if the (0,0) position of a volume is on or
in another existing object of a layer. Or check positions of all other centroids
and if the distance is within a certain length, then there already exists an existing
item.
