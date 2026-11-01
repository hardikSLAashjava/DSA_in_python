nums = [1,3,5,6]
target = 2

for i in range(len(nums)):
            if target in nums:
                    if nums[i] == target:
                        print(i)
            else:
                   if target > nums[i]:
                    print(i + 1)