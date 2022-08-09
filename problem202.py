class Solution:
    def isHappy(self, n):
        visited = [n]
        sq = {"1":1,"2":4,"3":9,"4":16,"5":25,"6":36,"7":49,"8":64,"9":81,"0":0}
        happy = False
        while(True):
            x = str(n)
            n=0
            for i in x:
                n += sq[i]
            if(n==1):
                happy=True
                break
            if(n in visited):
                break
            else:
                visited.append(n)
        return happy