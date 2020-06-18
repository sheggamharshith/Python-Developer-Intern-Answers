#Write a function that takes a path to a txt file as input and returns a list containing the number of words and sentences in the file. 
#Sample input - some txt file containing 10 lines and 100 words
#Sample output - [100,10]

import re 
text = " "
with open('/Users/harshithsheggam/Desktop/python_test/just.text','r') as f:
    text = " ".join([l.strip() for l in f.readlines()])

def getNumbers(str): 
    """ this method return list of numbers in str"""
    list_of_numbers = re.findall(r'[0-9]+', str) 
    list_of_numbers  = list(map(int,list_of_numbers))
    return list_of_numbers

if __name__ == "__main__":
    print(getNumbers(text))