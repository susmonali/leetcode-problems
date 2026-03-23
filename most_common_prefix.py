class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                if word==prefix:
                    prefix = word
                else:
                    prefix= prefix[:-1]
        
        return prefix

print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
print(Solution().longestCommonPrefix(strs = ["flower","aflow","flight", "felight"]))
print(Solution().longestCommonPrefix(strs = ["dog","racecar","car"]))
print(Solution().longestCommonPrefix(strs = ["a"]))
print(Solution().longestCommonPrefix(strs = ["a", "ab"]))
print(Solution().longestCommonPrefix(strs = ["ab", "acb", "afbv", "abf"]))