class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer = 0
        length = 0
        temp_len = 0
        visited = []
        while(pointer<len(s)):
            if(s[pointer] not in visited):
                temp_len += 1
                visited.append(s[pointer])
                if(pointer == len(s)-1):
                    if(temp_len > length):
                        length = temp_len
                pointer+=1
            else:
                pointer -= (len(visited)-visited.index(s[pointer])-1)
                if(temp_len > length):
                    length = temp_len
                visited = []
                temp_len = 0
        return length