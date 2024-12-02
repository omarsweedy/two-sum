from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,j in enumerate(nums):     
           diff = target-j
           if diff in hashmap:
             return [hashmap[diff],i] 
           hashmap[j]=i 
        return   






nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))