#Write a function find_longest_word() that takes a list of words and returns the length of the longest one

text="my name is astha and i love pragyaaaaaaaaaa"longest=0
for word in text.split():
        if len(word) > longest:
                longest=len(word)
                longest_word=wordprint("longest word is %s:" %longest_word)
print("longest word is %s:" %longest_word)


'''Output 
python nineteen.py
longest word is pragyaaaaaaaaaa:  '''
