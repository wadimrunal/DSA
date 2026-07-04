class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current width
            width = right - left
            
            # Calculate water capacity for current container
            current_water = min(height[left], height[right]) * width
            
            # Update max water found so far
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water