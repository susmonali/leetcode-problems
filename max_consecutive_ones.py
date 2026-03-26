class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_count = 0
        for i in nums:
            if i == 1:
                l+=1
            else:
                l=0
            if l>max_count:
                max_count = l
        return max_count
    
print(Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(Solution().findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))