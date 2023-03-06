# Longest Substring Without Repeating Characters

## Description
Given a string s, find the length of the longest 
substring without repeating characters.
 

#### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
#### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
#### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

#### Constraints:

- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

<br />

### Link to leetcode:  
https://leetcode.com/problems/longest-substring-without-repeating-characters/


## Solutions

### Brute Force
The brute force approach involves checking all possible substrings of the given string s and finding the longest substring without repeating characters. We can use two nested loops to generate all possible substrings and then use a set to check if there are any repeating characters in the substring. If there are no repeating characters, we update the max_length variable with the length of the substring.

In terms of time complexity, this approach has a worst-case time complexity of O(n^3) since we are generating all possible substrings and then checking each substring for repeating characters using a set. However, this approach can be useful when the input size is small and we need a quick solution.

```python
class Solution:
    def length_of_longest_substring(s: str) -> int:
        n = len(s)
        max_length = 0
        for i in range(n):
            for j in range(i, n):
                if len(set(s[i:j+1])) == j-i+1:
                    max_length = max(max_length, j-i+1)
        return max_length
```
To test this code, you can simply do the following:
```python
s = "abcabcbb"
print(Solution.length_of_longest_substring(s)) 
```
This code should output 3, which is the length of the longest substring without repeating characters in the given string.


