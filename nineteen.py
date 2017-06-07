
#Write a function find_longest_word() that takes a list of words and returns the length of the longest one

def find_longest_word():
   list1 = ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','asthaaaaaa',]
   max1 = ''
   for x in range (0, len(list1)):
      if (len(max1) < len(list1[x]) ):
          max1 = list1[x]
   return max1    


def main():
    m = find_longest_word()
    print len(m)

'''Output 
python nineteen.py
asthaaaaaa:  '''
