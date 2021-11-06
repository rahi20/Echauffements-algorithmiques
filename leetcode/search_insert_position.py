# Prob 35 Easy : Search Insert Position

from typing import List

class Solution:
    #Using binary search
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0 
        end = len(nums) - 1
        mid = 0
        while end >= start :
            mid = ( start + end )//2
            if target == nums[mid] : 
                return mid 
            elif target >= nums[mid] : 
                start = mid + 1
            else : 
                end = mid - 1


        return start

sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))

print(sol.searchInsert(nums = [1,3,5,6], target = 2))