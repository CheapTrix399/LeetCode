# INCOMPLETE SOLUTION .. TLE
class NumArray:  
    def __init__(self, nums: List[int]):
        self.matrix = []
        for i in range(len(nums)):
            new_arr = [None]*len(nums)
            new_arr[i] = nums[i]
            self.matrix.append(new_arr)
        for j in range(1,len(nums)):
            for i in range(0,j):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[j][j]

    def update(self, index: int, val: int) -> None:
        change = val - self.matrix[index][index]
        for i in range(index+1):
            for j in range(index,len(self.matrix)):
                self.matrix[i][j] += change

    def sumRange(self, left: int, right: int) -> int:
        return self.matrix[left][right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)