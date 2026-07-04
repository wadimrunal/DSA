class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for index, num in enumerate(nums):
            c = target - num
            if c in n:
              return [n[c], index]
            
        # Store current number index
            n[num] = index
        
        return []
