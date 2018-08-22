#### The base of getting images on Screen!!!

import kGraphicsMath as kg
import itertools
import array
from math import pi
import math


#Set Image size for the output image as a tuple. 
imRes = (100,100)
output_img = [[100,0,0] for i in range(imRes[0]*imRes[1])]

#function for setting pixels on screen. 
def set_pixel(x,y,colorVector):
	global output_img
	output_img[kg.getPixel((x,y),imRes)] = colorVector

def naiveLine(point1, point2, color):
	delta_x = point2[0] - point1[0]
	delta_y = point2[1] - point1[1]

	
	if delta_x == 0:
		print('vertical line detected')
		#vertical line

		delta_y = abs(delta_y)

		start_y = max(point2[1],point1[1])
		while delta_y > 0:
			set_pixel(point1[0],start_y,color)
			start_y -= 1
			delta_y -=1

	
	elif delta_y == 0:
		print('horizontal line detected')
		#horizontal line
		delta_x = abs(delta_x)

		start_x = max(point2[0],point1[0])
		while delta_x > 0:
			set_pixel(start_x,point1[1],color)
			start_x -= 1
			delta_x -=1

		pass



	else:
		slope = delta_y/delta_x

		
		if abs(slope) > 1:
			#Steep case
			pass


		else:
			#Shallow case
			pass






#Favorite colors
Blue = [0,0,255]
Green = [0,255,0]
White = [255,255,255]


set_pixel(90,28,Green)
set_pixel(60,10,[10,40,150])

naiveLine((50,30),(50,94),White)
naiveLine((50,60),(30,60),White)

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




