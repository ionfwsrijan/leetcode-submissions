class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hp1={}
        hp2={}
        for c in s1:
            if c in hp1:
                hp1[c]+=1
            else:
                hp1[c]=1
        
        left,right=0,0
        while right<len(s2):
            if s2[right] in hp2:
                hp2[s2[right]]+=1
            else:
                hp2[s2[right]]=1
            if (right-left+1)>len(s1):
                hp2[s2[left]]-=1
                if hp2[s2[left]] == 0:
                    del hp2[s2[left]]
                left+=1
            if (right-left+1)==len(s1):
                if hp1==hp2:
                    return True
            right+=1
        return False
