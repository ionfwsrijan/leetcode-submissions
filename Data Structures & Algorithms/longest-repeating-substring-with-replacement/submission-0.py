class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hp={}
        ans=0
        maxFreq=0
        left,right=0,0
        while right<len(s):
            if s[right] not in hp:
                hp[s[right]]=1
            else:
                hp[s[right]]+=1
            maxFreq = max(maxFreq, hp[s[right]])
            if (right-left+1)-maxFreq>k:
                hp[s[left]]-=1
                left+=1
            ans=max(ans,(right-left+1))
            right+=1
        return ans


