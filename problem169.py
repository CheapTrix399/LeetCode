class Solution:
    def majorityElement(self, nums):
        count = {}
        check = int(len(nums)/2)
        for i in nums:
            if(i in count.keys()):
                count[i] += 1
            else:
                count[i] = 1
            if(count[i]>check):
                return i