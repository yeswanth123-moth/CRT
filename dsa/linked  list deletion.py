class Node:
    def _init_(self,data):
        self.data=data
        self.next = None
class Linked_list:
    def _init_(self):
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
    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next
    def e_delete(self):
        if self.head is None or self.head.next==None:
            self.head=None
            return
        cur=self.head
        while  cur.next.next:
            cur=cur.next
        cur.next=None
    def b_delete(self):
        if self.head:
            self.head=self.head.next      
obj = Linked_list()
obj.b_insert(8)
obj.b_insert(10)
obj.e_insert(36)
obj.display()
print()
obj.b_delete()
obj.display()
