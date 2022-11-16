''' SQUARES OF SORTED ARRAY 

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

def sortedSquares(self, nums):
    new = []
    for n in nums:
        new.append(n*n)
    return sorted(new)

    # O(n) 

## OPTIMIZED ##
def sortedSquares(self, nums):
    return sorted(n*n for n in nums)

    # O(n log n)
    