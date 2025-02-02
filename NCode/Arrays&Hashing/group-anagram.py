# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
#
# Input: strs = ["x"]
#
# Output: [["x"]]
# Example 3:
#
# Input: strs = [""]
#
# Output: [[""]]
# Constraints:
#
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        com = {}
        check = {}
        final = []

        # store each word into a dict of letters corresponding to values
        for word in strs:
            if word not in com:
                com[word] = {}
            for letter in word:
                if letter not in com[word]:
                    com[word][letter] = 1
                else:
                    com[word][letter] += 1

        for word in strs:
            alist = []
            pattern = com[word]
            for each in strs:
                if each in check:
                    continue
                elif com[each] == pattern:
                    alist.append(each)
                    check[each] = True
            if alist:
                final.append(alist)


        return final

# TC: O(n^2 * k)
# SC: O(n*k)

# Different approaches
# Sort and sublist O(n log n)
# make unique identifier for each string of words then use that to sublist
from collections import defaultdict
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # create a dict of list
        res = defaultdict(list)

        # iterate over each word
        for s in strs:
            # convert word to tuple of count of each letter (only works for lower case)
            count = [0] * 26

            # iterate over each letter in word
            for c in s:
                # increment count of letter
                # ord gives ascii value of letter and ord('a') gives 97 to make it 0 based
                count[ord(c) - ord('a')] += 1
            # based on index of a given count, append word to list after converting to tuple
            res[tuple(count)].append(s)

        # return the values of res in an outer list
        return list(res.values())

# TC: O(n * k)
# SC: O(m)

# call the function
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution2().groupAnagrams(strs))
