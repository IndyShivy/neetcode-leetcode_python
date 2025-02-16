# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
#
# The test cases are generated such that the answer is always unique.
#
# You may return the output in any order.
#
# Example 1:
#
# Input: nums = [1,2,2,3,3,3], k = 2
#
# Output: [2,3]
# Example 2:
#
# Input: nums = [7,7], k = 1
#
# Output: [7]
# Constraints:
#
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
from collections import defaultdict


class Solution1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # need to find out a way to store the count of each number in an ordered way
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        top = []

        for i, num in counts.items():
            top.append([num, i])

        top.sort()

        fin = []
        while len(fin) < k:
            fin.append(top.pop()[1])
        return fin

#TC : O(nlogn) (O(n) for counting the frequency of each element and O(nlogn) for sorting the elements)
#SC : O(n)
