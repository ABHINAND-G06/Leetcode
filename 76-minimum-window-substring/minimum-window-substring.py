class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,have,need=0,0,0,0
        res=[-1,-1]
        if t=="" or s=="":return ""
        if len(s)<len(t):
            return ""
        wlen=float("inf")
        hashS=dict()
        hashT=dict()
        for c in set(t):
            hashS[c]=0
            hashT[c]=t.count(c)
            need+=1
        while(r<len(s)):
            ch=s[r]
            if ch in hashS:
                hashS[ch]+=1
                if hashS[ch]==hashT[ch]:
                    have+=1
            while(have==need):
                if r-l+1<wlen:    
                    wlen=r-l+1
                    res=[l,r+1]
                if s[l] in hashS:
                    hashS[s[l]]-=1
                    if hashS[s[l]]<hashT[s[l]]:
                        have-=1
                l+=1
            r+=1
        l,r=res
        return s[l:r]