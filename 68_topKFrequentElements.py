"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = {}
        ans = []
        for x in nums:
            if x in lis:
                lis[x] += 1
            else:
                lis[x] = 1

        slis = sorted(lis.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            ans.append(slis[i][0])

        return ans