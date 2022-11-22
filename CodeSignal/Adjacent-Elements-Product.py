'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
'''

def solution(inputArray):       
    start = inputArray[0] * inputArray[1]   # start with product of first two elements
    
    for i in range(1, len(inputArray) - 1):  # iterate thru remaining elements starting from second (idx 1) and ending at last element
        current = inputArray[i] * inputArray[i + 1]  # store product of next 2 items
        if current > start:    # compare start and current products, if current is greater..
            start = current    # update value of start with current product
            
    return start    


## OR ## 

def solution(inputArray):
    
    products = []
    
    for i in range(len(inputArray)-1):

        products.append(inputArray[i]*inputArray[i+1])
    
    return max(products)


## OPTIMIZED ##

def solution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])