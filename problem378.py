class Solution:
    def kthSmallest(self, matrix, k):
        ans = []
        pointer_arr = [0]*len(matrix)
        while(len(ans)<k):
            min_current = None
            pointer_x = None
            for pointer in range(len(matrix)):
                if(pointer_arr[pointer] >= len(matrix[pointer])):
                    continue
                if(min_current == None):
                    min_current = matrix[pointer][pointer_arr[pointer]]
                    pointer_x = pointer
                else:
                    if(min_current > matrix[pointer][pointer_arr[pointer]]):
                        min_current = matrix[pointer][pointer_arr[pointer]]
                        pointer_x = pointer
            pointer_arr[pointer_x] += 1
            ans.append(min_current)
        return ans[-1]