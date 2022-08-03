class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ""
        min_len = len(min(strs))
        for x in range(min_len):
            stop = 0
            char = strs[0][x]
            for word in strs:
                if(char != word[x]):
                    stop = 1
                    break
            if(stop == 0):
                ans += char
            else:
                break
        return ans