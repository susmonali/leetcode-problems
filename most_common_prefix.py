class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixs = []
        prefix = ""
        for index in range(len(strs)):
            if index+1 < len(strs) and strs[index][:1] == strs[index+1][:1] or len(strs) == 1:
                if index+1 < len(strs) and strs[index][:2] == strs[index+1][:2]:
                    prefixs.append(strs[index][:2])
                else:
                    prefixs.append(strs[index][:1])
        
        if len(prefixs)>=1:    
            return max(prefixs)
        else:
            return ""
print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))
print(Solution().longestCommonPrefix(strs = ["flower","aflow","flight", "felight"]))
print(Solution().longestCommonPrefix(strs = ["dog","racecar","car"]))
print(Solution().longestCommonPrefix(strs = ["a"]))
print(Solution().longestCommonPrefix(strs = ["a", "ab"]))
print(Solution().longestCommonPrefix(strs = ["ab", "acb", "afbv", "abf"]))