class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hp={None:None}
        
        curr=head
        while curr:
            copy=Node(curr.val)
            hp[curr]=copy
            curr=curr.next

        curr=head
        while curr:
            copy=hp[curr]
            copy.next=hp[curr.next]
            copy.random=hp[curr.random]
            curr=curr.next

        return hp[head]