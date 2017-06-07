#.Write a program that accepts a sentence and calculate the number of letters and digits.
            
s = raw_input("Input a string\n")
d=l=0
for c in s:
    if c.isdigit(): 
       d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


'''Output 
python eleventh.py
Input a string
asthajain
('Letters', 9)
('Digits', 0)'''
