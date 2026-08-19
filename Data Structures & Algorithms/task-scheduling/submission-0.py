class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        freq=[c for c in count.values()]
        heapq.heapify_max(freq)
        time=0
        q=deque()
        while freq or q:
            time+=1
            if freq:
                cnt=heapq.heappop_max(freq)-1
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                heapq.heappush_max(freq,q.popleft()[0])

        return time