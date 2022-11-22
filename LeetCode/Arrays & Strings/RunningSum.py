''' Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''


#### BRUTE FORCE SOLUTION #### O(n^2)

def runningSum(nums):
    sums = []                   # array to keep track of sums

    for i in range(len(nums)):  # iterate thru elements in nums
        run_sum = 0             # keeps track of running sum

        for j in range(i+1):    # iterate thru elements after i
            run_sum += nums[j]  #sum of all elements up to nums[i]
        sums.append(run_sum)    # add runing sums to sums array

    return sums


#### LIST COMPREHENSION SOLUTION #### O(n^2)

def runningSum(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]  # same a snested for loop above, finds running sum up to i


#### IMPROVED SOLUTION #### O(n)

def runningSum(nums):

    for i in range(1, len(nums))  # iterate thru elements starts at index 1
        nums[i] = nums[i] + nums[i -1]
    
    return nums


