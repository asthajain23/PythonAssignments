#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

str=raw_input("\nenter string\n")
if(str==str[::-1]):
        print("string is palindrome")
else:
        print("string is not palindrome")


'''Output
 python twenty.py
enter string
madam
string is palindrome'''
