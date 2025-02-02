# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false

# Logic
         # convert list to set
         # if set length is less than array: return true
         # else : return false

class Solution1:
    def hasDuplicate(self, nums: list[int]) -> bool:
        mySet = set(nums)
        if len(mySet) != len(nums):
            return True
        else:
            return False

# TC: Set : O(n) : AvgC = O(n), BestC = O(1)

# SC: O(n)


# Alternate solution
class Solution2:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()  # O(n log n)
        for i in range(len(nums) - 1):  # O(n)
            if nums[i] == nums[i + 1]:
                return True
        return False

# TC:
# Sorting : O(n log n)
# Loop : O(n)
# Final: O(n log n)


# SC:
# Array : O(n)
# Fin  : 0(n)


