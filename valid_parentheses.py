class Solution:
    def isValid(self, s: str) -> bool:
        openings = ["(", "{", "["]
        endings = [")", "}", ]
        q = []
        i=0
        while i < len(list(s)):
            if s[i] in openings and s[i+1] not in endings:

                q.append(s[i])
            i+=1
        return q
        # return len(list(s))
        
print(Solution().isValid(s = "([)]"))
print(Solution().isValid(s = "([])"))
print(Solution().isValid(s = "(]"))
print(Solution().isValid(s = "()[]{}"))
