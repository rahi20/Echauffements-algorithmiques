#Eaasy Prob 1: Two Sum

from typing import List

def two_sum(nums: List[int], target: int)-> List[int]:
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in map.keys():
            return [i, map[complement]]
        map[nums[i]] = i


print(two_sum([1,2,34,52,12,0,12,2], 3))