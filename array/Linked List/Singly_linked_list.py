class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def append(head, val):
    node = Node(val)
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node

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


if __name__ == "__main__":
    head = Node(None)

    for val in ['A', 'B', 'C', 'D']:
        append(head, val)

    for node in gen(head):
        print(node.val, end=' ')
        print(node)
node = search(head,"B")
print(node)
def delete(head,val):
    cur = head.next
    prev = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
            return
        prev = cur
        cur = cur.next
delete(head,"B")
for no in gen(head):
    print(no.val,end=" ")
def clear(self):
    self.head = None
    self.size = 0
