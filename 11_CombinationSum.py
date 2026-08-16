"""
Given an array of distinct integers, candidates and a target integer, target
return a list of all unique combinations of candidates where the chosen numbers sum to target.
** the same number may be chosen from candidates an unlimited number of times
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        def backtracking(cur, i):
            s = sum(cur)
            if s == target:
                sol.append(cur)
            elif s < target:
                for j in range(i, len(candidates)):
                    backtracking(cur + [candidates[j]], j)

        backtracking([], 0)

        return sol