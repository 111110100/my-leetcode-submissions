class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums: list, target: int): 
        d = {}
        for i, v in enumerate(nums):
            m = target - v
            if m in d:
                return [d[m], i]
            else:
                d[v] = i

nums = [2, 7, 11, 15]
target = 9

answer = Solution()
print(answer.twoSum(nums, target))

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
