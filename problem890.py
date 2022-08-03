class Solution:
    def num_hash(self,word):
        uniq_words = []
        hash = ""
        for w in word:
            if(w not in uniq_words):
                uniq_words.append(w)
            hash += str(uniq_words.index(w))
        return hash
    def findAndReplacePattern(self, words, pattern):
        ans = []
        p_num_hash = self.num_hash(pattern)
        for word in words:
            if(self.num_hash(word) == p_num_hash):
                ans.append(word)
        return ans