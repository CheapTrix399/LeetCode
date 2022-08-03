class Solution:
    def romanToInt(self, s):
        ans = 0
        x=0
        while(x<len(s)):
            if(s[x]=="I"):
                if(x == len(s)-1):
                    ans += 1
                    x+= 1
                else:
                    if(s[x+1]=="V"):
                        ans += 4
                        x += 2
                    elif(s[x+1]=="X"):
                        ans += 9
                        x += 2
                    else:
                        ans += 1
                        x += 1
            elif(s[x]=="V"):
                ans += 5
                x += 1
            elif(s[x]=="L"):
                ans += 50
                x += 1
            elif(s[x]=="D"):
                ans += 500
                x += 1
            elif(s[x]=="M"):
                ans += 1000
                x += 1
            elif(s[x]=="X"):
                if(x == len(s)-1):
                    ans += 10
                    x+= 1
                else:
                    if(s[x+1]=="L"):
                        ans += 40
                        x += 2
                    elif(s[x+1]=="C"):
                        ans += 90
                        x += 2
                    else:
                        ans += 10
                        x += 1
            elif(s[x]=="C"):
                if(x == len(s)-1):
                    ans += 100
                    x+= 1
                else:
                    if(s[x+1]=="D"):
                        ans += 400
                        x += 2
                    elif(s[x+1]=="M"):
                        ans += 900
                        x += 2
                    else:
                        ans += 100
                        x += 1
        return ans