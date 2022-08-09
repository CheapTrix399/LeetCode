class Solution:
    def trailingZeroes(self, n):
        ans = 0
        i = 1
        while((n/(5**i)) >= 1):
            ans += int(n/(5**i))
            i += 1
        return ans