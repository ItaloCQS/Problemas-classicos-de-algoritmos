class Solution(object):
    def twoSum(self, nums, target):
        bli = {}
        
        for index, value in enumerate(nums):
            key = target - value
            if key in bli:
                return bli[key], index
            else:
                bli[value] = index
         
        
nums = [1,5,2,3] 
target = 5 

print(Solution().twoSum(nums,target))


