# Write a function that will take a string as input and return a new string without consonants.
# Sample input - “abc”
# Same output = “a”
def remove_consonants(input_str):
    """ This Function takes a string return a string that is free from consonants"""
    vowels= ['a','e','i','o','u']
    final_ans = ""
    for char in input_str:
        if char in vowels:
            final_ans+=char
    return final_ans
if __name__ == "__main__":
    input_str = input("please enter the string")
    ## invoking the method remove consonants 
    str_after_modification = remove_consonants(input_str)
    print(str_after_modification)