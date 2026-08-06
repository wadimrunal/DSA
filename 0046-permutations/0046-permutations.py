class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
        
            for i in range(start, len(nums)):
            # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
            
            # Recurse for the next position
                backtrack(start + 1)
            
            # Backtrack by swapping the elements back
                nums[start], nums[i] = nums[i], nums[start]
            
        backtrack(0)
        return result