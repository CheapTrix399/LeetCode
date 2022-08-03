class Solution:
    def plusOne(self, digits):
        rev_arr = digits[::-1]
        carry = 1
        for index in range(len(rev_arr)):
            if(carry == 0):
                break
            sum_d = rev_arr[index]+carry
            rev_arr[index] = sum_d%10
            carry = int(sum_d/10)
        if(carry>0):
            rev_arr.append(carry)
        return rev_arr[::-1]