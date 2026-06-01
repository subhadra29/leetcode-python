#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets={
            "[":"]",
            "{":"}",
            "(":")"
        }
        stack=[]
        for i in s:
            if(i=="(" or i=="[" or i=="{"):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                top=stack[-1]
                if(brackets[top]==i):
                    stack.pop()
                else:
                    return False
        return len(stack)==0
            
            
                
            
            
        
                
                

        
# @lc code=end

