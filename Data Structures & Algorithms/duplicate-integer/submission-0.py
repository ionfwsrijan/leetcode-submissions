class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp={}
        for i in range(len(nums)):
            if nums[i] in hp:
                hp[nums[i]]+=1
            else:
                hp[nums[i]]=1
        
        for value in hp.values():
            if value>1:
                return True

        return False
