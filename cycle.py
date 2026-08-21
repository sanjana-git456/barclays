class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
nodes = [ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6), ListNode(7)]

nodes[0].next = nodes[1]  # 1 -> 2
nodes[1].next = nodes[2]  # 2 -> 3
nodes[2].next = nodes[3]  # 3 -> 4
nodes[3].next = nodes[4]  # 4 -> 5
nodes[4].next = nodes[5]  # 5 -> 6
nodes[5].next = nodes[6]  # 6 -> 7
nodes[6].next = nodes[3]  # 7 -> back to 4 (this is what creates the cycle)

head = nodes[0]
def cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            p2 = head
            while p2 != slow:
                p2 = p2.next
                slow = slow.next
            return p2
    return False
result = cycle(head)
print(result.val)