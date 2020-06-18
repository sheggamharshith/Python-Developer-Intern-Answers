# Given a number (greater than 2), print two prime numbers whose sum will be equal to the given number, else print -1 if no such number exists. 
# 
# Sample input - [1,2,3,4], K=2
#Sample output -
#[1,2]
#[2,1]
#[3,4]
#[4,3]

# method for geting subarray
def getSub(Sum, i, j):  
  
    if i == 0: 
        return Sum[j]  
    else: 
        return Sum[j] - Sum[i - 1]  
  
 
def maxsuboverlap(arr, N, K):  
    """Method prints two non-overlapping subarrays  of length K whose Sum is maximum  """
  
    Sum = [None] * N 
  
    # filling prefix Sum array  
    Sum[0] = arr[0]  
    for i in range(1, N):  
        Sum[i] = Sum[i - 1] + arr[i]  
  
    # Initializing subarrays from 
    # (N-2K) and (N-K) indices  
    resinx = (N - 2 * K, N - K)  
  
    # initializing result Sum from above subarray Sums  
    max2sub = (getSub(Sum, N - 2 * K, N - K - 1) + 
                       getSub(Sum, N - K, N - 1))  
  
    # storing second subarray maximum and its starting index  
    secondSubarrayMax = (N - K, getSub(Sum, N - K, N - 1))  
  
    # looping from N-2K-1 towards 0  
    for i in range(N - 2 * K - 1, -1, -1):  
      
        # get subarray Sum from (current index + K)  
        cur = getSub(Sum, i + K, i + 2 * K - 1)  
  
        # if (current index + K) Sum is more  
        # than update secondSubarrayMax  
        if cur >= secondSubarrayMax[1]: 
            secondSubarrayMax = (i + K, cur)  
  
        # now getting complete Sum (Sum of both subarrays)  
        cur = (getSub(Sum, i, i + K - 1) + 
                           secondSubarrayMax[1])  
  
        # If it is more then update main result  
        if cur >= max2sub: 
          
            max2sub = cur  
            resinx = (i, secondSubarrayMax[0])  
  
    # printing actual subarrays  
    for i in range(resinx[0], resinx[0] + K):  
        print(arr[i], end = " ")  
    print()  
  
    for i in range(resinx[1], resinx[1] + K):  
        print(arr[i], end = " ")  
    print()

if __name__ == "__main__": 
  
    #for static values 
    arr = [1,2,3,4]  
    N = len(arr) 
    K = 2
    maxsuboverlap(arr, N, K)  

    # for dyanmic values uncomment below
    #arr = list(map(int,input("please enter the numbers").split()))
    #N = len(list_of_numbers)
    #k = int(input("roatations"))
    #printMax(list_of_numbers, n, k) 