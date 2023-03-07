'''
Optimized Sliding Window Solution
All other solutions to the question can be found in the README.md documentation.
'''

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