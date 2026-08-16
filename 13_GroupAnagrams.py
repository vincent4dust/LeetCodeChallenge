"""
Given an array of string strs, group the anagrams together
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Intuition:
1. initializing variables
start by initiliazing an empty unordered map, mp which store the groups of anagrams

2. group anagrams
iterate through each word in the input vector strs.
i. sort the word
create a string variable, word and assign the sorted characters
ii. group the anagram
push the key, values into mp

3. create the result
create variable, ans
iterate mp and push the values into ans

4. return result
return ans
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word in mp:
                mp[word].append(i)
            else:
                mp[word] = []
                mp[word].append(i)
            
        ans = []
        if len(mp) > 0:
            for k, v in mp.items():
                ans.append(v)

        return ans