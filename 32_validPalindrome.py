"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        non_alpha = ""
        sym = "~!@#$%^&*()_+`-=[]\{}|;':\",./<>? "
        for i in s:
            if i not in sym:
                non_alpha += i.lower()

        stack = []
        temp = ""
        for i in non_alpha:
            stack.append(i)

        for i in range(len(stack)):
            temp += stack.pop()

        if non_alpha == temp:
            return True
        else:
            return False
        

# bitwise negation to compare char
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))