#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        
        k=1
        total=0
        if(n==2):
            return 2
        while (n-(2*k))>=1:
            nums=math.factorial(k+(n-(2*k)))/(math.factorial(k) * math.factorial((n-(2*k))))
            total+=int(nums)
            k=k+1
        if(n%2==0):
            total=total+2
        else:
            total=total+1
        return (total)







        

        
# @lc code=end

