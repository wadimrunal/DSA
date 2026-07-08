class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0  # Left boundary of the sliding window
    
        for end in range(len(s)):
            current_char = s[end]
        
        # If the character is already in our map and its index is within 
        # the current window, contract the window by moving start past it
            if current_char in char_map and char_map[current_char] >= start:
                start = char_map[current_char] + 1
            
        # Update the character's last seen position
            char_map[current_char] = end
        
        # Calculate the current window size and update max_length
            max_length = max(max_length, end - start + 1)
        
        return max_length
