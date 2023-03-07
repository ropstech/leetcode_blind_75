
class Solution:
    def length_of_longest_substring(s: str) -> int:
        n = len(s)
        chars = set()
        i, j = 0, 0
        max_length = 0
        while i < n and j < n:
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                max_length = max(max_length, j-i)
            else:
                chars.remove(s[i])
                i += 1
        return max_length
    
s = "abcabcbb"
print(Solution.length_of_longest_substring(s)) 