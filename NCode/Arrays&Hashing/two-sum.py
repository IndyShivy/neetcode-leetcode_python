class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        check = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in check:
                return [check[comp], i]
            check[num] = i

        return []

# TC: O(n)
# SC: O(n)
