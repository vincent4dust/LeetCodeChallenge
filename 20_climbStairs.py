"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
Tabulation method:
A bottom-up approach to solve the problem iteratively. It creates a DP table of size n+1 to store the number of ways to reach each step.
The base cases are initialized to 1 since there is only one way to reach them. Then, it iterates from 2 to n,
filling the DP table by summing up the values for the previous two steps.

DP[n] = DP[n-1] + DP[n-2]
DP[n-1] needs to be applied 1 step to reach DP[n]
DP[n-2] needs to be applied 2 step to reach DP[n]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]