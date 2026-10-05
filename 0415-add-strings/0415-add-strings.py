class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        
        carry = 0
        result = []
        
        # Loop until both strings are processed AND there's no leftover carry
        while i >= 0 or j >= 0 or carry:
            # Get the digit value or 0 if the pointer has gone out of bounds
            # ord(char) - ord('0') safely converts a character digit to an integer
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Calculate column sum and new carry
            column_sum = digit1 + digit2 + carry
            carry = column_sum // 10
            
            # Store the single unit digit in our result list
            result.append(str(column_sum % 10))
            
            # Move both pointers to the left
            i -= 1
            j -= 1
            
        # The result list is built backwards, so reverse it and join to a string
        return "".join(result[::-1])