class Solution:
    def myAtoi(self, s: str) -> int:
        string = s.strip()
        mystr = ""
        if(string == ""):
            return 0
        if((string[0]=="-")|(string[0]=="+")):
            mystr += string[0]
            string = string[1:]
        for x in string:
            if(x.isnumeric()):
                mystr += x
            else:
                break
        if((mystr == "")|(mystr == "+")|(mystr == "-")):
            return 0
        mystr = int(mystr)
        if(mystr < -(2**31)):
            return -(2**31)
        elif(mystr > ((2**31) - 1)):
            return ((2**31) - 1)
        else:
            return mystr