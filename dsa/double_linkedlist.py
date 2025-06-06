class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_linkedlist:
    def __init__(self):
        self.head=self.tail=None

    def b_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head =self.tail= newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head =self.tail= newnode
            return
        newnode.prev = self.tail
        self.tail.next = newnode
        self.tail = newnode

    def forward_display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    def backward_display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.tail
        while cur:
            print(cur.data, end="->")
            cur = cur.prev
    def b_delete(self):
        if self.head == self.tail:
            self.head = self.tail =None
        if self.head:
            self.head = self.head.next
            self.head.prev=None

    def e_delete(self):
        if self.head == self.tail:
            self.head = self.tail =None
        if self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

    def position(self,pos):
        cur = self.head
        for i in range(pos-1):
            if cur.next is None:
                break
            cur = cur.next
        else: return cur


    def position_insert(self,data,pos):
        if pos == 1:
            self.b_insert(data)
            return
        cur = self.position(pos)
        # if cur == self.tail:
        #     self.e_insert(data)
        #     return
        newnode = Node(data)
        if cur:
            newnode.next = cur
            newnode.prev = cur.prev
            cur.prev = newnode.prev.next = newnode

    def position_delete(self, pos):
        if pos == 1:
            self.b_delete()
            return
        cur = self.position(pos)
        if cur == self.tail:
            self.e_delete()
            return
        if cur:
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            cur.prev=cur.next=None


obj = Double_linkedlist()
obj.e_insert(6)
obj.e_insert(10)
obj.e_insert(30)
obj.b_insert(5)
obj.forward_display()
print()
obj.backward_display()
obj.position_delete(2)
print()
obj.forward_display()
print()
obj.backward_display()