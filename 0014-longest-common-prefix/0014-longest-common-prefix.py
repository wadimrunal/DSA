class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        # Sort the array alphabetically
        strs.sort()
    
    # Compare the first and last strings
        first = strs[0]
        last = strs[-1]
        result = []
    
    # Find characters that match from the beginning
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])
        return "".join(result)
    
