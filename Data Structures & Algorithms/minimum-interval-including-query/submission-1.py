from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        num_intervals = len(intervals)
        num_queries = len(queries)

        intervals.sort()

        indexed_queries = sorted(
            (query_value, index) 
            for index, query_value in enumerate(queries)
        )

        result = [-1] * num_queries

        min_heap = []
        interval_index = 0

        for query_value, original_index in indexed_queries:

            while interval_index < num_intervals and intervals[interval_index][0] <= query_value:
                start, end = intervals[interval_index]
                interval_size = end - start + 1

                heappush(min_heap, (interval_size, end))
                interval_index += 1

            while min_heap and min_heap[0][1] < query_value:
                heappop(min_heap)

            if min_heap:
                result[original_index] = min_heap[0][0]

        return result