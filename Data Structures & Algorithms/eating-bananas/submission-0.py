class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        mink=r
        while l<=r:
            totalhrs=0
            mid=(l+r)//2
            for p in piles:
                hrs=math.ceil(p/mid)
                totalhrs+=hrs
            if totalhrs<=h:
                mink=min(mink,mid)
                r=mid-1
            else:
                l=mid+1

        return mink  