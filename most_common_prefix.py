class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        

        for s in strs[1:]:
            
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
print(Solution().longestCommonPrefix(strs = ["flower","aflow","flight", "felight"]))
print(Solution().longestCommonPrefix(strs = ["dog","racecar","car"]))
print(Solution().longestCommonPrefix(strs = ["a"]))
print(Solution().longestCommonPrefix(strs = ["a", "ab"]))
print(Solution().longestCommonPrefix(strs = ["ab", "acb", "afbv", "abf"]))