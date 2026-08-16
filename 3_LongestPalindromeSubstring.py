# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         maxS = ""
#         n = len(s)
#         for i in range(n):
#             for j in range(i, n):
#                 li = s[i:j+1]
#                 k = len(li)
#                 tmp = ""
#                 while(k):
#                     tmp += li[k-1]
#                     k -= 1
#                 if li == tmp and len(tmp) > len(maxS):
#                     maxS = li
#         return maxS

"""
Function P: P(i,j) = True if s[i:j] is palindromic; False if s[i:j] is not palindromic
Thus, P(i,j) = P(i+1, j-1) and s[i] == s[j]
Base cases are
P(i,i) = True
P(i,i+1) = (s[i] == s[i+1])
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s
        res = ""
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[j][i] = True
                elif j == i+1:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (dp[j-1][i+1] and s[i] == s[j])
                if dp[j][i] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res

solution = Solution()
# s = "babad"
# s = "cbbd"
s = "a"
maxS = solution.longestPalindrome(s)
print(maxS)