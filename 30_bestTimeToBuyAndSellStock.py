"""
Given an array prices where prices[i] is the price of a given stock on the ith day
you want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.
Return the max profit you can achive from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        current = prices[0]
        profit = -1

        for i in range(1, len(prices)):
            if prices[i] < current:
                current = prices[i]
            elif prices[i] - current > profit:
                profit = prices[i] - current

        if profit < 0: profit = 0

    return profit       