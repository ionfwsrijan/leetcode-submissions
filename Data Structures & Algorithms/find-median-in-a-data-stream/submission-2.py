from heapq import heappush, heappop
class MedianFinder:

	def __init__(self):
        # the smaller half of the list, max heap (invert min-heap)
		self.smallerHalf = []
        # the larger half of the list, min heap
		self.largerHalf = []

	def addNum(self, num: int) -> None:

		# trick for smaller half, use -1*val
		# heapq in python does NOT have comparator like in Java
		heappush(self.smallerHalf, -num)
		heappush(self.largerHalf, -heappop(self.smallerHalf)) # note: not self.smallerHalf.pop()

		if len(self.smallerHalf) < len(self.largerHalf):
			heappush(self.smallerHalf, -heappop(self.largerHalf))

	def findMedian(self) -> float:
		if len(self.smallerHalf) == len(self.largerHalf):
			return (-self.smallerHalf[0] + self.largerHalf[0]) / 2.0
		else:
			return float(-self.smallerHalf[0])