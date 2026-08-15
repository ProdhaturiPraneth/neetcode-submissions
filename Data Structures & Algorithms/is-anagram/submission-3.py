class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs={}
        ht={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hs:
                hs[s[i]]=1
            else:
                hs[s[i]]+=1
            if t[i] not in ht:
                ht[t[i]]=1
            else:
                ht[t[i]]+=1
        return ht==hs