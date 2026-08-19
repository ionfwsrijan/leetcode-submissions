class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hp1={}
        hp2={}
        if len(s)==len(t):
            for i in s:
                if i in hp1:
                    hp1[i]+=1
                else:
                    hp1[i]=1

            for j in t:
                if j in hp2:
                    hp2[j]+=1
                else:
                    hp2[j]=1
            if hp1==hp2:
                return True
            else:
                return False
        else:
            return False
