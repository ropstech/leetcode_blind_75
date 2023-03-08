from typing import List

class Solution:
    def two_sum_hash_table(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[nums[i]] = i
        return None

s = Solution()
number_list = [1, 3, 5, 7, 8, 9]
target_number = 13

result = s.two_sum_hash_table(number_list, target_number) # Result will be [2, 4]
