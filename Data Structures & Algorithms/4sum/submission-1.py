class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 0, 4)

    def kSum(self, nums: List[int], target: int, start: int, k: int) -> List[List[int]]:
        res = []
        if start == len(nums) or nums[start] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return self.twoSum(nums, target, start)
        for i in range(start, len(nums)):
            if i == start or nums[i - 1] != nums[i]:
                for sset in self.kSum(nums, target - nums[i], i + 1, k - 1):
                    res.append([ nums[i] ] + sset)
        return res

    def twoSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        res = []
        lo, hi = start, len(nums) - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target or (lo > start and nums[lo] == nums[lo - 1]):
                lo += 1
            elif s > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res