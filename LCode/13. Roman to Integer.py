class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L":50,"XL": 40, "X": 10, "IX": 9, "V": 5,
               "IV": 4, "I": 1}
        total = 0
        loop_off = False
        for i in range(0, len(s)):
            if not loop_off:
                if i != len(s)-1:
                    if s[i] + s[i + 1] in dic:
                        total += dic[s[i] + s[i + 1]]
                        loop_off = True
                    else:
                        total += dic[s[i]]
                else:
                    total += dic[s[i]]
            else:
                loop_off = False
        return total

    def romanToInt2(self, s: str) -> int:
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L":50,"XL": 40, "X": 10, "IX": 9, "V": 5,
               "IV": 4, "I": 1}
        total = 0
        # use a while loop
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in dic:
                total += dic[s[i:i+2]]
                i+=2
            else:
                total += dic[s[i]]
                i+=1
        return total

sol = Solution()
print(sol.romanToInt2("IV"))
