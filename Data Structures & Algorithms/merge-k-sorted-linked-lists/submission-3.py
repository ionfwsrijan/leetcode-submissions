import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))

        dummy = cur = ListNode()

        while pq:
            val, i, node = heapq.heappop(pq)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
        return dummy.next