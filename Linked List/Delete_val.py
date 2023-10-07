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
for node in ["A","D","B"]:
    append(head,node)
def gen(head):
    cur = head.next
    while cur :
        yield cur
        cur = cur.next
    return
print("ORIGNAL LINKED LIST:")
for node in gen(head):
    print(node.val,end=" ")
def remove(head,val):
    cur = head.next
    prev = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
            return
        prev = cur
        cur = cur.next
remove(head,"B")
print("\nThe new list is :")
for node in gen(head):
    print(node.val , end=" ")

