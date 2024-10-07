class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        
        total = 0
        
        for i in range(len(s)):
           
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
           
            else:
                total += roman_to_int[s[i]]

        return total

# Example usage
solution = Solution()

# Test cases
print(solution.romanToInt("III"))      
print(solution.romanToInt("LVIII"))    
print(solution.romanToInt("MCMXCIV"))  
