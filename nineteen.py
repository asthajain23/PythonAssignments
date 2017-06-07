
#Write a function find_longest_word() that takes a list of words and returns the length of the longest one

def main ():
    text = raw_input("Please input a List of words to evaluate: ")

    longest = 0

    for words in text.split():
           if len(words) > longest:
                  longest = len(words)
    print ("The longest word is", words, "with lenght", longest)


main()

'''Output 
python nineteen.py
asthaaaaaa:  '''
