class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
head = Node(None)
def append(head,val):
    node = Node(val)
    cur = head
    while cur.next :
        cur = cur.next
    cur.next = node
for node in [1,2,3,4,5,6,7]:
    append(head,node)
def gen(head):
    cur = head.next
    while cur :
        yield cur
        cur= cur.next
    return
print("ORIGNAL LINKED LIST:")
for node in gen(head):
    print(node.val , end=" ")
def calculate_sum(head):
    sum = 0
    for node in gen(head):
        sum += node.val
    return sum
print("\nThe sum is :", calculate_sum(head))

