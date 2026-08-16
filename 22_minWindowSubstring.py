"""
Given two strings s and t of lengths m and n respectively, return the min window substring of s such that every char in t (including duplicates)
is included in the window. If there is no such substring, return the empty string ""
"""

# 1. init t_counter and window to keep track of char counts in t and current window
# 2. populate t_counter by iterating through the char of t and incrementing their counts
# 3. define have to track how many required char we have in our current window
# and need to represent the total number of char requried
# 4. set left as 0
# 5. iterate through s using a right pointer
# 6. enter a loop while we have all required char in our window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        t_counter , window = {} , {}

        for x in t:
            t_counter[x] = 1 + t_counter.get(x , 0)

        have , need = 0 , len(t_counter)
        ans , ans_size = [-1 , -1] , float("infinity")  
        left = 0

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right] , 0)

            if s[right] in t_counter and window[s[right]] == t_counter[s[right]] :
                have += 1

            while have == need :
                if (right - left + 1) < ans_size:
                    ans = [left , right]  
                    ans_size = (right - left + 1)

                window[s[left]] -= 1
                if s[left] in t_counter and window[s[left]] < t_counter[s[left]] :
                    have -= 1
                left += 1

        return s[ans[0] : ans[1]+1] if ans_size != float("infinity") else ""  