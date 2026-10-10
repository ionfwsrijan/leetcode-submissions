class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hp={}
        for n in nums:
            if n not in hp:
                hp[n]=1
            else:
                hp[n]+=1
        
        mf=max(hp.values())

        for k,v in hp.items():
            if v==mf:
                return k