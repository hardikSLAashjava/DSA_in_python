class Solution(object):
    # the nums and target are given
    def searchInsert(self, nums, target): 
        for i in range(len(nums)):
            if target in nums:
                #checks if the target is in the list and if the target is equal to the current number in the list, if so it returns the index of that number  
                if nums[i] == target:
                    return i
                #if the target is not in the list, it checks if the target is greater than the current number in the list, if so it returns the index of that number

            if target < nums[i]:
                return i
        #if the target is greater than all the numbers in the list, it returns the length of the list        
        else:
            return len(nums)
        