class Solution:
    def addDigits(self, num):
        while(num >= 10):
            temp = 0
            while(num>0):
                temp += num%10
                num = int(num/10)
            num = temp
        return num