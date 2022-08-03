class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1,2]
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            for x in range(3,n+1):
                ans.append(ans[-1]+ans[-2])
            return ans[-1]