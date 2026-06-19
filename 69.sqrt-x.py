#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        n=1
        k=x//n
        while (n<k):
            n=n+1
            k=x//n


            
        return k


        
        
# @lc code=end

