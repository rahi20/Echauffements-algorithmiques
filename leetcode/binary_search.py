#Prob Easy : Binary Search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = -1
        while end >= start :
            mid = (end + start) // 2
            if target == nums[mid] : 
                return mid
            elif target > nums[mid] :
                start = mid + 1
            else : 
                end = mid - 1

        return -1


sol = Solution()

print(sol.search(nums = [-1,0,3,5,9,12], target = 9))

