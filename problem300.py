class Solution:
    def lengthOfLIS(self, nums) -> int:
        ans = [0]*(len(nums)-1) + [1]
        left = len(nums)-2
        max_ans = 1
        while(left >= 0):
            temp = left+1
            temp_max = 0
            while(temp<len(nums)):
                if(nums[left]<nums[temp]):
                    if(ans[temp]>temp_max):
                        temp_max = ans[temp]
                temp += 1
            ans[left] = 1 + temp_max
            if(ans[left] > max_ans):
                max_ans = ans[left]
            left -= 1
        print(ans)
        return max_ans