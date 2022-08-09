class Solution:
    def countVowelPermutation(self, n):
        i=1
        x = {"a":1,"e":1,"i":1,"o":1,"u":1}
        while(i<n):
            a_new = x["e"]+x["i"]+x["u"]
            e_new = x["a"] + x["i"]
            i_new = x["e"] + x["o"]
            o_new = x["i"]
            u_new = x["i"] + x["o"]
            x["a"] = a_new
            x["e"] = e_new
            x["i"] = i_new
            x["o"] = o_new
            x["u"] = u_new
            i+=1
        ans = (x["a"] + x["e"] + x["i"] + x["o"] +x["u"]) % ((10**9) + 7)
        return ans