
class Solution:
    def length_of_longest_substring(s: str) -> int:
        n = len(s)
        max_length = 0
        for i in range(n):
            for j in range(i, n):
                print(j)
                print(n)
                if len(set(s[i:j+1])) == j-i+1:
                    max_length = max(max_length, j-i+1)
        return max_length
    
s = "abcabcbb"
print(Solution.length_of_longest_substring(s)) 