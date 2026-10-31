class Solution(object):
    def singleNumber(self, nums):
        repeating_elements = []
        for i in range(len(nums)):
            if nums[i] in repeating_elements:
                continue
                
            found = False
            
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    repeating_elements.append(nums[i])
                    found =True
                    break
            if found == False:
                return nums[i]