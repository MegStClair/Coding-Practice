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


''' FIND PIVOT INDEX 

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.'''

def pivotIndex(self, nums):
    
    left = 0
    right = sum(nums)
    
    for i, num in enumerate(nums):
        right -= num
        if left == right:
            return i
        else:
            left += num
            
    return -1

    # O(n)