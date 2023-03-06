from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        """
        Finds the indices of two numbers in the input list that add up to the target.

        Args:
            nums (List[int]): Input list of integers.
            target (int): Target sum.

        Returns:
            List[int]: List of two indices that add up to the target sum, or an empty list if no such pair exists.
        """
        if not nums:
            return []

        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]
                
        # if no two numbers add up to the target, return an empty list
        return []

s = Solution()
number_list = [1, 3, 5, 7, 8, 9]
target_number = 8

result = s.twoSum(number_list, target_number)

print(result)
