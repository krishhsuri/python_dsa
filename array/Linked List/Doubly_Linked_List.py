class Node(object):
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
def append(head,val):
    node = Node(val)
    cur = head
    while cur.next :
        cur = cur.next
    cur.next = node
    node.prev = cur
    return
def gen(head):

    cur = head.next
    while cur:
        yield cur
        cur = cur.next
def search(head,val):
    for node in gen(head):
        if node.val == val :
            return node
    return None
def delet(head,val):
    cur = head.next
    while cur.next:
        if cur.val == val :
            cur.prev.next = cur.next
            if cur.next :
                cur.next.prev = cur.prev
            return
        cur = cur.next

head = Node(None)



for val in ["A","B","C","D","E","F"]:
    append(head,val)
for node in gen(head):
    print(node.val ,end="\n")
node = search(head,"D")
delet(head,"C")
for n in gen(head):
    print(n.val, end=" ")