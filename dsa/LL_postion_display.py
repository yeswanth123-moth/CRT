class Node:
    def __init__(self,data):
        self.data=data
        self.next = None



class Linked_list:
    def __init__(self):
        self.head=None

    def b_insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode


    def e_delete(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None


    def b_delete(self):
        if self.head:
            self.head = self.head.next

    def pos_delete(self,pos):
        if pos == 1:
            self.b_delete()
            return
        cur = self.position(pos - 1)
        if cur and cur.next:
            cur.next = cur.next.next
        else:
            print("position not found")


    def position(self,pos):
        if pos<=0:
            print("invalid position")
            return

        cur = self.head
        for i in range(pos-1):
            if cur.next==None:
                break
            cur = cur.next
        else: return cur
    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    def pos_insert(self,data,pos):
        if pos == 1:
            self.b_insert(data)
            return
        newnode = Node(data)
        cur = self.position(pos-1)
        if cur:
            newnode.next = cur.next
            cur.next = newnode
        else: print("position not found")

obj = Linked_list()
obj.b_insert(10)
obj.e_insert(8)
obj.e_insert(36)
obj.display()
print()
obj.pos_delete(4)
obj.display()