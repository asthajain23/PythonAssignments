#Define a function that computes the length of a given list or string.

def length(object):#Define the length calculation function
    count = 0      
    object =raw_input("Enter the string")
    for i in object:
        count=count+1
    print("Length of the string is" +str(count))
    
 length(object)

'''Output
python tenth.py
Enter the stringasthaj
6'''
