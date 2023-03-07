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


### Sliding Window

```python
class Solution:
    def length_of_longest_substring(s: str) -> int:
        n = len(s)
        chars = set() # set to keep track of characters in current window
        i, j = 0, 0
        max_length = 0
        while i < n and j < n:
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                max_length = max(max_length, j-i)
            else:
                chars.remove(s[i]) # remove the leftmost character from set
                i += 1
        return max_length
```

The Sliding Window technique is a popular algorithmic approach that is often used to solve optimization problems. The general idea behind the Sliding Window technique is to create a window of some fixed size and slide it over the input data in order to solve the problem at hand.

In this solution, we maintain a sliding window of characters in the input string s such that the characters within the window are all unique. We initialize the window with the first character of the string and move the window to the right by one character at a time. If the character at the right end of the window is not already in the window, we add it to the window and update the maximum length of the window. If the character is already in the window, we remove the leftmost character from the window and move the window to the right.

This algorithm runs in O(n) time because we visit each character in the string at most twice (once when adding it to the set and once when removing it from the set). Therefore, it is much more efficient than the brute force algorithm we discussed earlier.


To test this code, you can use the same code as in the Brute Force Test:
```python
s = "abcabcbb"
print(Solution.length_of_longest_substring(s)) 
```

### Optimized Sliding Window
```python
class Solution:
    def length_of_longest_substring(s: str) -> int:
        n = len(s)
        char_dict = {}
        i, j = 0, 0
        max_length = 0
        while j < n:
            if s[j] in char_dict and i <= char_dict[s[j]]:
                i = char_dict[s[j]] + 1
            else:
                max_length = max(max_length, j - i + 1)
            char_dict[s[j]] = j
            j += 1
        return max_length
```

In this approach, instead of using a set to keep track of the unique characters in the current substring, we use a dictionary to keep track of the last seen index of each character.

The i pointer still represents the start of the current substring and the j pointer represents the end. We iterate through the string, moving j forward and updating the dictionary to store the last seen index of each character.

If we encounter a character that is already in the dictionary and its last seen index is greater than or equal to the current i, we update i to be one greater than the last seen index of the character, effectively "sliding" the window to exclude the previously seen occurrence of the character.

Otherwise, we update max_length to be the maximum of its current value and the length of the current substring (which is j - i + 1), and add the current character and its index to the dictionary.

I will go a little more into detail on what the following if statement is doing:
```python
if s[j] in char_dict and i <= char_dict[s[j]]:
```
In the if statement, we are checking if the current character s[j] is already in the dictionary chars and if its position is within the current window. We need to check if the position of the current character is within the current window because if it's outside the window, we don't need to consider it when we update the window.

The condition i <= chars[s[j]] checks if the position of the current character is greater than or equal to the start index of the current window (i). If it's less than i, it means the current character's position is outside the current window and we don't need to consider it. If it's greater than i, it means the current character's position is within the current window and we need to update the start index of the window to be one position to the right of the current position of the character in the dictionary. This is because we want to exclude the previous occurrence of the character from the current window, as we want to find the longest substring without repeating characters.

Overall, this approach has a time complexity of O(n), which is an improvement over the O(n^2) time complexity of the brute force approach and the O(n log n) time complexity of the normal sliding window approach.