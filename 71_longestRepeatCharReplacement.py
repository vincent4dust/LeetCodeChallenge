"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left_pointer = 0
        maxf = 0
        for index in range(len(s)):
            count[s[index]] = 1 + count.get(s[index], 0)
            maxf = max(maxf, count[s[index]])

            if (index - left_pointer + 1) - maxf > k:
                count[s[left_pointer]] -= 1
                left_pointer += 1
            res  = max(maxf, index - left_pointer + 1)
        return res