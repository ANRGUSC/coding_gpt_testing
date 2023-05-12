class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort() # sort the array
        closest_sum = float('inf') # initialize the closest sum to infinity
        
        for i in range(len(nums)-2): # loop through all possible triplets
            left = i+1 # initialize left pointer
            right = len(nums)-1 # initialize right pointer
            
            while left < right: # loop until pointers meet
                curr_sum = nums[i] + nums[left] + nums[right] # calculate current sum
                if abs(curr_sum - target) < abs(closest_sum - target): # update closest sum
                    closest_sum = curr_sum
                if curr_sum < target: # move left pointer
                    left += 1
                elif curr_sum > target: # move right pointer
                    right -= 1
                else: # if found exact target, return sum
                    return curr_sum
        
        return closest_sum # return closest sum if no exact sum is found