class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fixed=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                csum=nums[i]+nums[j]+nums[k]
                if csum==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1    
                elif csum>0:
                    k-=1
                else:
                    j+=1

        return res
        