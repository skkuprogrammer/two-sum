from typing import List
target = 0
nums = []
def twoSum(nums,target):
    list = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j > i:
                if nums[i]+nums[j] == target:
                    list.append(i)
                    list.append(j)
    print(list)
    
twoSum([2, 7, 11, 15], 9)
twoSum([3,2,4], 6)
twoSum([3,3], 6)