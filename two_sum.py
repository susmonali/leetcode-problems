# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         for num in enumerate(nums):
#             need = target-num[1]
#             for i in enumerate(nums):
#                 if i[0] != num[0]:
#                     if i[1] == need:
#                         result.append(num[0])
#                         result.append(i[0])
#                         return result
                
#             # return need

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in result:
                return [result[need], i]
            result[num]=i

print(Solution().twoSum(nums = [2,7,11,15], target = 9))