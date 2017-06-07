#Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]

def remove_even(l):
        for i in l:
                if i% 2==0:
                        l.remove(i)
        print l
        return l
remove_even([5,6,77,45,22,12,24])
remove_even([5,77,45,12])



'''Output
python sixteen.py
[5, 77, 45, 12]
[5, 77, 45]
'''
