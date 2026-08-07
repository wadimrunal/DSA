class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        t_factors = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                t_factors[p] += 1
                t //= p
        if t > 1:
            return "-1"  # t contains prime factors other than 2, 3, 5, 7
            
        digit_factors = {
            '1': (0, 0, 0, 0), '2': (1, 0, 0, 0), '3': (0, 1, 0, 0),
            '4': (2, 0, 0, 0), '5': (0, 0, 1, 0), '6': (1, 1, 0, 0),
            '7': (0, 0, 0, 1), '8': (3, 0, 0, 0), '9': (0, 2, 0, 0)
        }
        
        # Helper to find the minimum digits needed to satisfy required factors
        def get_min_digits(c2, c3, c5, c7):
            # 9s take two 3s
            n9 = c3 // 2
            rem3 = c3 % 2
            
            # 8s take three 2s
            n8 = c2 // 3
            rem2 = c2 % 3
            
            # Combine remaining 2s and 3s optimally
            res23 = []
            if rem3 == 1 and rem2 == 2:    # 3 and 4 -> 2 and 6
                res23 = [2, 6]
            elif rem3 == 1 and rem2 == 1:  # 3 and 2 -> 6
                res23 = [6]
            elif rem3 == 1 and rem2 == 0:  # 3
                res23 = [3]
            elif rem3 == 0 and rem2 == 2:  # 4
                res23 = [4]
            elif rem3 == 0 and rem2 == 1:  # 2
                res23 = [2]
                
            digits = [9] * n9 + [8] * n8 + [7] * c7 + [5] * c5 + res23
            digits.sort()
            return digits

        n = len(num)
        # Find the first occurrence of '0'
        z = num.find('0')
        if z == -1:
            z = n
            
        # Precompute prefix factor counts up to the first '0'
        pref_counts = [[0, 0, 0, 0] for _ in range(z + 1)]
        for i in range(z):
            f = digit_factors[num[i]]
            for j in range(4):
                pref_counts[i + 1][j] = pref_counts[i][j] + f[j]
                
        # If the number itself is zero-free and already valid
        if z == n:
            curr = pref_counts[n]
            if (curr[0] >= t_factors[2] and curr[1] >= t_factors[3] and 
                curr[2] >= t_factors[5] and curr[3] >= t_factors[7]):
                return num

        # Step 2: Search from right to left for the longest common prefix match
        for i in range(z, -1, -1):
            if i == n:
                continue
            
            # Determine starting digit to try
            start_d = 1 if i == z and z < n else int(num[i]) + 1
            
            for d in range(start_d, 10):
                f = digit_factors[str(d)]
                # Remaining factors needed from t
                rem_2 = max(0, t_factors[2] - (pref_counts[i][0] + f[0]))
                rem_3 = max(0, t_factors[3] - (pref_counts[i][1] + f[1]))
                rem_5 = max(0, t_factors[5] - (pref_counts[i][2] + f[2]))
                rem_7 = max(0, t_factors[7] - (pref_counts[i][3] + f[3]))
                
                needed_digits = get_min_digits(rem_2, rem_3, rem_5, rem_7)
                rem_len = n - 1 - i
                
                if len(needed_digits) <= rem_len:
                    # Construct the smallest suffix matching the length constraint
                    ones_padding = '1' * (rem_len - len(needed_digits))
                    suffix = ones_padding + "".join(map(str, needed_digits))
                    return num[:i] + str(d) + suffix
                    
        # Step 3: If no prefix of the same length works, expand the length
        min_t_digits = get_min_digits(t_factors[2], t_factors[3], t_factors[5], t_factors[7])
        target_len = max(n + 1, len(min_t_digits))
        
        ones_padding = '1' * (target_len - len(min_t_digits))
        return ones_padding + "".join(map(str, min_t_digits))