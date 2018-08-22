#All your graphics related math functions.




def getPixel(loc,dimensions):
	# x + width*y
	return loc[0] - dimensions[0]*loc[1]