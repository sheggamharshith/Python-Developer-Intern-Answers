#Given a list L and integer K, find the maximum for each and every contiguous subarray of size K. Write a function that takes the list as input and returns the output as a list.
# Sample input - [8, 5, 10, 7, 9, 4, 15, 12, 90, 13] , K = 4
#Sample output - [10, 10, 10, 15, 15, 90, 90]



def printMax(list_of_numbers, n, k): 
    max = 0
    final_list = []
    for i in range(n - k + 1): 
        max = list_of_numbers[i] 
        for j in range(1, k): 
            if list_of_numbers[i + j] > max: 
                max = list_of_numbers[i + j] 
        final_list.append(max)
    print(final_list)
  
# Driver method 
if __name__=="__main__": 
    list_of_numbers = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    n = len(list_of_numbers) 
    k = 4
    printMax(list_of_numbers, n, k) 

    # for dyanmic values uncomment below
    #list_of_numbers = list(map(int,input("please enter the numbers").split()))
    #n = len(list_of_numbers)
    #k = int(input("roatations"))
    #printMax(list_of_numbers, n, k) 

  