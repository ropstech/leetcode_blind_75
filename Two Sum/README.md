# Two Sum

## Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
<br />
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.  
<br />
#### Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
#### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

#### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
<br />

#### Constraints:

- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- Only one valid answer exists.

<br />

### Link to leetcode:  
https://leetcode.com/problems/two-sum/

## Solutions

### Brute Force

```python
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum_brute_force(nums, target))  # Output: [0, 1]
```

The brute force method involves checking every pair of elements in the array to see if their sum equals the target. This can be done using two nested loops, where the outer loop iterates through each element in the array, and the inner loop iterates through the remaining elements to find a pair that adds up to the target. If such a pair is found, we can return its indices.

While this method is simple to implement, it is not very efficient in terms of time complexity. The time complexity of this approach is O(n^2), where n is the size of the array. This is because we need to iterate through the array twice to check every possible pair of elements.

### Hash Table

```python
def two_sum_hash_table(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum_hash_table(nums, target))  # Output: [0, 1]
```

The hash table approach involves storing each element of the array in a hash table along with its index. Then, we can iterate through the array and check if the complement of each element (i.e., target - element) exists in the hash table. If it does, we can return the indices of the two elements.

The time complexity of this approach is O(n), where n is the size of the array. This is because we only need to iterate through the array once to check each element's complement in the hash table. In the best case, where we find the two elements right away, the time complexity would be O(1). In the worst case, where we have to iterate through the entire array, the time complexity would be O(n).

### Sorting the Array

```python
def two_sum_sort(nums, target):
    nums_sorted = sorted(nums)
    start, end = 0, len(nums_sorted) - 1
    while start < end:
        curr_sum = nums_sorted[start] + nums_sorted[end]
        if curr_sum == target:
            return [nums.index(nums_sorted[start]), nums.index(nums_sorted[end])]
        elif curr_sum < target:
            start += 1
        else:
            end -= 1
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum_sort(nums, target))  # Output: [0, 1]
```

The sorting approach involves sorting the array first and then using two pointers to find the two elements that add up to the target. We can use one pointer at the beginning of the array and another pointer at the end of the array. If the sum of the two elements is greater than the target, we move the end pointer to the left. If the sum is less than the target, we move the start pointer to the right. We continue this process until we find the two elements.

The time complexity of this approach is O(nlogn), where n is the size of the array. This is because we need to sort the array first, which takes O(nlogn) time complexity. After sorting, we only need to iterate through the array once to find the two elements using the two pointers. The best case scenario is also O(1), where the target is found right away at the start and end of the array. The worst case scenario is when we iterate through the entire array, which would take O(n) time complexity.