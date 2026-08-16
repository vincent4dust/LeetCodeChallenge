# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         def check(start, end):
#             chars = [0] * 128
#             for i in range(start, end + 1):
#                 c = s[i]
#                 chars[ord(c)] += 1
#                 if chars[ord(c)] > 1:
#                     return False
#             return True

#         n = len(s)

#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if check(i, j):
#                     res = max(res, j - i + 1)
#         return res

class Solution:
    def lengthOfLongestSubstring(self, s):
        maxL = 0
        start = 0
        i = 0
        li = ""
        while i < len(s):
            if s[i] in li:
                maxL = max(maxL, len(li))
                start = s.index(s[i], start) + 1
                li = s[start: i+1]
            else:
                li += s[i]

            i += 1
        maxL = max(maxL, len(li))
        return maxL

solution = Solution()
s = "aujkk"
res = solution.lengthOfLongestSubstring(s)
print(res)