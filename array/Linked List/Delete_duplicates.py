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
for node in ["A","A","D","D","B","B"]:
    append(head,node)
# LINKED LIST CREATED
def gen(head):
    cur = head.next
    while cur:
        yield cur
        cur= cur.next
    return
print("ORIGNAL LINKED LIST:")
for node in gen(head):
    print(node.val,end=" ")

def remove_dup(head):
    if not head or not head.next :
        return None
    def itera(head):
        current = head
        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    return itera(head)
remove_dup(head)
print("\n The new list is :")
for node in gen(head):
    print(node.val , end=" ")
