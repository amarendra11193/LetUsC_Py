# The length and breadth of a rectangle and radius of a circle are input through the keyboard. Write a program to calculate the area and perimeter of the rectangle, and the area and cirumference of the circle.

def area_rect(length, breadth):
	area = float(length*breadth)
	return round(area,2)
	
def perim_rect(length, breadth):
	perimeter = float(2*(length + breadth))
	return round(perimeter,2)

def area_cir(radius):
	area = float(3.14*radius**2)
	return round(area,2)
	
def perim_cir(radius):
	perimeter = float(2*3.14*radius)
	return round(perimeter,2)
	
l = float(input('Enter the Length of the Rectangle: \n'))
b = float(input('Enter the Breadth of the Rectangle: \n'))
r = float(input('Enter the Radius of the Circle: \n'))
print('The Area of the Rectangle is: ', area_rect(l,b))
print('The Perimeter of the Rectangle is: ', perim_rect(l,b))
print('The Area of the Circle is: ', area_cir(r))
print('The Perimeter of the Circle is: ', perim_cir(r))