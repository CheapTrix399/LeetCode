class Solution:
    def isPalindrome(self, s):
        return s==s[::-1]
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s),0,-1):
            for index in range(0,len(s)-length+1):
                if(self.isPalindrome(s[index:index+length])):
                    return s[index:index+length]