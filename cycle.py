# Definition for singly-leaked list.
class LinkedListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Plan/Psuedocode
# 1) Initialize two pointers (slow and fast) at beginning of list
# 2) Iterate over the LinkedList as long as the slow and fast pointers don't overlap
# 3) Check if there are nodes to travel to:
    # if fast's next node OR fast's next next node are Null, return False
    # else
        # move slow pointer 1 node forward
        # move fast pointer 2 nodes forward
# 4) return True when cycle found (slow == fast)

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head   # slow mover
    fast = head.next   # fast mover pointer
    while fast is not None and fast.next is not None:
        # break loop if slow and fast pointers meet
        if slow == fast:
            return True

        else:
            slow = slow.next  # move by 1 node
            fast = fast.next.next  # move by 2 nodes
    return False  # no cycle!


# build a LinkedList to test code
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1 # created a cycle
print(hasCycle(node1)) # should return True

node1 = LinkedListNode(1)
print(hasCycle(node1)) # should return False

node1 = None
print(hasCycle(node1)) # should return False

