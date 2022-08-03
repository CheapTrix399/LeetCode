class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid = True
        for a in set(s+t):
            if(s.count(a)!=t.count(a)):
                valid = False
        return valid