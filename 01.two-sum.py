
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
output=[]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for a in range(len(nums)):
            for i in range(a+1,len(nums)):
                if(nums[a] + nums[i] == target):
                    return[a,i]

        
# @lc code=end

