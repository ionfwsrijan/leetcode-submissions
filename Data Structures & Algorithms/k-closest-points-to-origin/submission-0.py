class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for point in points:
            x,y=point
            d=math.sqrt((x*x)+(y*y))
            dist.append((d,point))
        heapq.heapify_max(dist)
        while len(dist)>k:
            heapq.heappop_max(dist)
        
        return [point for d, point in dist]