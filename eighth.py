#Define a function max() that takes two numbers as arguments and returns the largest of them

def largerValue(a, b): 
	if a > b:       
	print(str(a) +'is larger than' + str(b))    
else:        
	print (str(b) +' is larger than ' + str(a))

print ('Enter the first number')
aA = input()
print ('Enter the second number')
bB = input()

largerValue(aA,bB) 


'''Output
python eighth.py
Enter the first number21
Enter the second number36
36 is larger than 21'''                  
