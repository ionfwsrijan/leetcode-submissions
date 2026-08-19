class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        nums_set=set(nums)
        for curr in nums_set:
            if curr-1 not in nums_set:
                count=1
                while curr+1 in nums_set:
                    curr+=1
                    count+=1
                longest=max(longest,count)
        return longest