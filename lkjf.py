
nums = [1,11,1,2,2,2,3]
unique = []
duplicate = 0

for i in range(len(nums)):
        if nums[i] not in unique:
            unique.append(nums[i])
        else:
            duplicate += 1

print(duplicate,unique)
        