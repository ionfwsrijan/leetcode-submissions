class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hp={}
            for i in range(len(nums)):
                if nums[i] in hp:
                    hp[nums[i]]+=1
                else:
                    hp[nums[i]]=1
            
            res=sorted(hp,key=hp.get,reverse=True)[:k]
            return res