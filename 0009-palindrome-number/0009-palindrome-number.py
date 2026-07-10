class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
    
    # Loop until we have processed at least half of the digits
        while x > reversed_half:
        # Pop the last digit from x and append it to reversed_half
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
        
    # If the number has an odd number of digits, we can get rid of the middle digit 
    # by doing reversed_half // 10 (since the middle digit doesn't matter for palindromes)
        return x == reversed_half or x == reversed_half // 10
