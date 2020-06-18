
# Write a function to check whether the string is a palindrome. 
# The function should take a string as input. 
# If found to be a palindrome, 
# print “is palindrome” 
# else print “not palindrome”.
# Sample input - “noon”
# Sample output- “is palindrome”

#creating a function for checking palindrome
def is_Palindrome(input_string):
    """This function takes input as string and returns True if its a palindrome else false if not """

    # taking advantage of python 
    if input_string == input_string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    # taking input() from user
    input_str = input("please enter the string for palindrome")
    # invoking the palindrome 
    if is_Palindrome(input_str):
        print("is  palindrome")
    else:
        print("not  palindrome")




