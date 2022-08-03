class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if(x == "("):
                stack.append(x)
            elif(x=="{"):
                stack.append(x)
            elif(x=="["):
                stack.append(x)
            elif(x==")"):
                if(len(stack)>0):
                    if(stack[-1]=="("):
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    return False
            elif(x=="}"):
                if(len(stack)>0):
                    if(stack[-1]=="{"):
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    return False
            elif(x=="]"):
                if(len(stack)>0):
                    if(stack[-1]=="["):
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False