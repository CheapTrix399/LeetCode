class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        needle_len = len(needle)
        if(len(needle)==0):
            return 0
        else:
            for i in range(len(haystack)-needle_len+1):
                if(haystack[i:i+needle_len]==needle):
                    return i
        return ans