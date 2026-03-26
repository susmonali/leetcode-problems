class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = []
        response = []
        if nums[0] >1:
            for i in range(len(nums), 0, -1):
                numbers.append(i)
        else:
            for i in range(1, len(nums)+1):
                numbers.append(i)
        for i, num in enumerate(nums):    
            if numbers[i]!=num and nums[i]==nums[i-1]:
                response.append(nums[i-1])
                response.append(numbers[i])
        return response
    
print(Solution().findErrorNums(nums = [1,2,2,4]))
print(Solution().findErrorNums(nums = [1,1]))
print(Solution().findErrorNums(nums = [3,2,2]))

