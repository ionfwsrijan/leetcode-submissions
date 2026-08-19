class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hp:
                if hp[diff]<i:
                    return [hp[diff],i]
                else:
                    return [i,hp[diff]]
            else:
                hp[nums[i]]=i
                