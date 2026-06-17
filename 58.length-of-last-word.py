#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=[]
        for word in s.split():
            words.append(word)
        damn=words.pop()
        return len(damn)

        
# @lc code=end

