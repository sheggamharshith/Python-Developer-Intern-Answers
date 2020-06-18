# Write a function that will take a sentence as input in the form of a string. 
# Remove all but the first occurrence of every duplicate word in the sentence. 
# Return the modified sentence.
# 	Sample input - “I write code. I love to code.”
# 	Same output- “I write code. I love to.”


# creating a python function that removes the first occurrence  
def removeFirstOccur(input_string):
    # creating a empty list
    final_list = []

    # making an assumption that string is a case sensitive 
    # if not uncommnet the below code
    #org_list = input_string.lower()
    # not sure with the question you meant with word or stop words
    org_list = input_string.split()
    #print(org_list)
    count = 0
    for item in org_list:
        if item in final_list and count<1 and len(item)>3: # not sure the with the question word should be length of or should i use nlp for that
            count+=1
        else:
            final_list.append(item)

    #print(final_list)
    ans =  " ".join(final_list)
    return ans
    

str1 = input("Please enter your own String : ")
#char = input("Please enter your own Character : ")

print("Original String :  ", str1)
print("Final String :     ", removeFirstOccur(str1))