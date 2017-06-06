#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them

def biggest (a, b, c):
	imax = a
	if (b > imax) and (b > c):
		imax = b    
	elif (c > imax):
		imax = c    
	return imax 

print (biggest(5,6,7))


'''Output
python ninth.py
7'''
