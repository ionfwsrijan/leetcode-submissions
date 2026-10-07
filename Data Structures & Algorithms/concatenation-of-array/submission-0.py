class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nc=nums.copy()
        res=nums
        for i in nc:
            res.append(i)
        return res