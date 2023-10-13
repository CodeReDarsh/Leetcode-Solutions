# good solution 1 (solution I came up with):
class Solution1:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        smap = {}
        for i in range(len(s)):
            if s[i] in smap and smap[s[i]] != t[i]: return False
            smap[s[i]] = t[i]
        my_set = set()
        for a in smap:
            if smap[a] in my_set: return False
            my_set.add(smap[a])
        return True
    
# crazy good solution 2 (this is like 1 liner and kinda cheating kinda not lol?)
class Solution2:
    def isIsomorphic2(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))