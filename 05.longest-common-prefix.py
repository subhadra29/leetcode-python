#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=0
        word=""
        count=0
        for i in strs[0]:
            count=0
            for j in strs:
                if(a>(len(j)-1)):
                    return word
                if(str(i) != str(j[a])):
                    return word

                if(str(i) == str(j[a])):
                    count+=1

                if(count == len(strs)):
                    word+=str(i)
                    

            a+=1
        return word

        
                

                




        



        




        
# @lc code=end

