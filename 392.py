class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        slen = len(s)
        while i < slen and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1

        return i == slen