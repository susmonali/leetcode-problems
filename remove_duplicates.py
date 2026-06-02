class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        k = 0
        previous = None
        for i in nums:
            if i != previous:
                result.append(i)
                k+=1
            previous = i

        for q in range(len(nums)-len(result)):
            result.append("_")

        return result
    
print(Solution().removeDuplicates(nums = [1,1,2]))
print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
