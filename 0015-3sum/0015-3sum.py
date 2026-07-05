class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
    
    # 1. Sort the array to group duplicate integers together
        nums.sort()
        n = len(nums)
    
        for i in range(n - 2):
        # Early Pruning: If the current number is positive, since the list is sorted, 
        # any subsequent numbers will also be positive, making a zero sum impossible.
            if nums[i] > 0:
                break
            
        # Skip duplicate values for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
        # Initialize two pointers for the remaining sub-array
            left = i + 1
            right = n - 1
        
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                
                # Advance left and retract right while skipping identical duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1  # Sum is too small, move left pointer to a larger value
                else:
                    right -= 1  # Sum is too large, move right pointer to a smaller value
                
        return result
