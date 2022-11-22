
''' FIND PIVOT INDEX 

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.'''

def pivotIndex(self, nums):
    
    left = 0            # initiate left at 0
    right = sum(nums)   # right side is the sum of nums
    
    for i, num in enumerate(nums):  # enumerate thru nums
        right -= num                # remove current num from right, leave in limbo since we dont want to include it
        if left == right:           # check for equality
            return i                # if equal, return that index (pivot index)
        else:
            left += num             # if not equal, add num to left side
            
    return -1                       # if both sides are never equal, return last index as pivot index (per instructions)

    # O(n)