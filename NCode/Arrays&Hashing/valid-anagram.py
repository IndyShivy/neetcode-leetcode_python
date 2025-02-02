# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
# Constraints:
#
# s and t consist of lowercase English letters.

# both string into dictionary
        # compare dict

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        com = {}
        comp = {}

        for letter in s:
            if letter not in com:
                com[letter] = 1
            else:
                com[letter] += 1

        for letter in t:
            if letter not in comp:
                comp[letter] = 1
            else:
                comp[letter] += 1

        if com == comp:
            return True
        else:
            return False

# TC : O(n+m)
# SC : O(1)

# Alternate solution
from collections import Counter

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Only for lower case
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Quick check to avoid unnecessary computation
            return False

        count = [0] * 26  # Array for 'a' to 'z'

        for letter in s:
            count[ord(letter) - ord('a')] += 1  # Increase frequency

        for letter in t:
            count[ord(letter) - ord('a')] -= 1  # Decrease frequency

        return all(c == 0 for c in count)  # If all counts are zero, it's an anagram






