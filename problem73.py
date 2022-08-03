class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if(matrix[x][y]==0):
                    for x1 in range(len(matrix)):
                        if(matrix[x1][y] != 0):
                            matrix[x1][y] = "C"
                    for y1 in range(len(matrix[0])):
                        if(matrix[x][y1] != 0):
                            matrix[x][y1] = "C"
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if(matrix[x][y]=="C"):
                    matrix[x][y] = 0