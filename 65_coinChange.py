"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

"""
Approach
We define a class Solution with a function coinChange that takes in a list of coins and an integer amount as input and returns an integer, which is the fewest number of coins required to make up the amount.

We define a list dp of length amount + 1. dp[i] represents the fewest number of coins needed to make up the amount i.

We initialize the first element of dp to be 0 (since 0 coins are needed to make up an amount of 0). We also initialize the rest of the elements to amount + 1, which is an arbitrary value greater than the maximum amount we can have.

We loop through each coin in the coins list and for each coin, we loop through all amounts from the coin value up to the amount and update dp[i] as the minimum of the current dp[i] and dp[i - coin] + 1.

We return -1 if dp[amount] is amount + 1, which means we were not able to make up the amount with the given coins. Otherwise, we return dp[amount], which is the fewest number of coins required to make up the amount.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]