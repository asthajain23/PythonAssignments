#Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old\

name = raw_input("What is your name: ")
age = int(raw_input("How old are you: "))
year =str((2017 - age)+100)
print(name + " will be 100 years old in the year " + year)

'''Output
python sixth.py
What is your name: astha
How old are you: 21
astha will be 100 years old in the year 2096 '''
