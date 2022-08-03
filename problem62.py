class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if((m<=0) | (n<=0)):
            return 0
        matrix = []
        arr = [1] + [1]*(n-1)
        matrix.append(arr)
        for x in range(m-1):
            arr = [1] + [0]*(n-1)
            matrix.append(arr)
        for x in range(1,m):
            for y in range(1,n):
                matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]
        return matrix[m-1][n-1]