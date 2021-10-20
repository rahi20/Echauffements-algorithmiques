from typing import List

class Solution:
    #Double loop
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)

        #if strs is empty 
        if n == 0 : 
            return ""

        #strs not empty
        k = 0
        #Increment the index, it stops at the shortest str 
       
        while True :
            str_idx = 0
            longest_common_prefix = ""            
            char_to_check = ""
            for i in range(n):
                if len(strs[i]) <= str_idx : 
                    return longest_common_prefix
                if strs[i][str_idx] != char_to_check :
                    return longest_common_prefix
                longest_common_prefix += char_to_check
                str_idx += 1 

        # str_idx = 0
        # longest_common_prefix = ""            
        # char_to_check = ""
        # for i in range(n):
        #     if len(strs[i]) <= str_idx : 
        #         return longest_common_prefix
        #     if strs[i][str_idx]

sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))