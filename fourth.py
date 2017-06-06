#Write a Python program to count the number of lines in a text file

import io
fo =open("astha.txt","w+")
fo.write("hello\nastha\njain\nzensar")
fo.close()
filename="astha.txt"
myfile = open(filename)
lines = len(myfile.readlines())
print "There are %d lines in %s" % (lines, filename)

'''Output
python fourth.py
There are 4 lines in astha.txt '''
