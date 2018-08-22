#### The base of getting images on Screen!!!

import kGraphicsMath as kg
import itertools
import array
from math import pi
import math

#Fake enum for visual learning reasons. 
X = 0
Y = 1

#Set Image size for the output image as a tuple. 
imRes = (100,100)
output_img = [[100,0,0] for i in range(imRes[0]*imRes[1])]

#function for setting pixels on screen. 
def set_pixel(x,y,colorVector):
	"""
	sets color of 
	"""
	global output_img
	output_img[kg.getPixel((x,y),imRes)] = colorVector

def dda_line(point1,point2,color):
	"""
	dda line drawing algorithm for learning purposes
	"""

	#Get difference between 2 points
	deltaX = point2[X] - point1[X]
	deltaY = point2[Y] - point1[Y]


	#Calculate how many times you need to draw pixels to make the line. (steps)

	if abs(deltaX) > abs(deltaY): 
		Steps = abs(deltaX)
	else:
		Steps = abs(deltaY)


	#Calculate the increment in x coordinatesand y coordinates.

	Xincrement = deltaX / Steps
	Yincrement = deltaY / Steps

	#Set starting point for pixels to be from starting point 1:
	xval = point1[X]
	yval = point1[Y]

	for step in range(Steps-1):
		xval += Xincrement
		yval += Yincrement
		set_pixel(int(xval),int(yval),color)





#Favorite colors
Blue = [0,0,255]
Green = [0,255,0]
White = [255,255,255]


dda_line([90,28],[60,10],White)

set_pixel(90,28,Green)
set_pixel(60,10,Blue)



#output_img[kg.getPixel((20,5),imRes)] = [0,10R0,100]R

#Circle with radius of 8. Located at 50,65























#PPM TIME
ppm_header = 'P6 {} {} 255\n'.format(imRes[0],imRes[1])
#Base image
image = array.array('B', list(itertools.chain.from_iterable(output_img)))
 
#WRITE OUT FILE
with open('output.ppm', 'wb') as f:
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)




