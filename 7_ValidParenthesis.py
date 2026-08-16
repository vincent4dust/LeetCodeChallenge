"""
Given a string s containing just chars '(', ')', '{', '}', '[', ']'
determine if the input string is valid

An input string is valid if:
- open brackets must be closed by the same type of brackets
- open brackets must be closed in the correct order
- every close bracket has a corresponding open bracket of the same type
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        return not stack