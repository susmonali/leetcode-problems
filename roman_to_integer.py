class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i in range(len(s)):
            value = roman_to_int[s[i]]
            if i + 1 < len(s) and roman_to_int[s[i+1]]>value:
                result-=value
            else:
                result+=value

        return result
    
print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
