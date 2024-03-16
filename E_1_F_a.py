# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees.

def fahr_to_cent(temp):
	temp = float((temp - 32)*5/9)
	return round(temp,2)
	
temp = float(input('Enter the Temperature in Fahrenheit: \n'))
print('The Temperature in Centigrade degrees: ', fahr_to_cent(temp)