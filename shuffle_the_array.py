class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(0, n):
            result.append(nums[:n][i])
            result.append(nums[n:][i])

        return result
    

print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))
print(Solution().shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(Solution().shuffle(nums = [1,1,2,2], n = 2))
