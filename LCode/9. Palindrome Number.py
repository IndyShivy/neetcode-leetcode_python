class Solution:
    def isPalindrome(self, x) -> (bool):
        con = str(x)
        print(con[::-1])
        if con == con[::-1]:
            return True
        return False


x = "Totast"
sol = Solution()
# Output: True
print(sol.isPalindrome(x))
