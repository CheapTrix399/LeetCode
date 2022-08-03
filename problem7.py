class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            ans = int("-"+str(x)[1:][::-1])
            if(ans < -2147483648):
                return 0
            else:
                return ans
        else:
            ans = int(str(x)[::-1])
            if(ans >= 2147483648):
                return 0
            else:
                return ans