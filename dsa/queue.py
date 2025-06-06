class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def display(self):
        if len(self.queue)==0:
            print("empty")
            return
        for i in self.queue:
            print(i,end=" ")
    def dequeue(self):
        if len(self.queue) == 0:
            print("empty")
            return
        self.queue.pop(0)
    def front(self):
        if len(self.queue) == 0:
            print("empty")
            return
        print(self.queue[0])
obj = Queue()
obj.enqueue(18)
obj.enqueue(7)
obj.display()
obj.dequeue()
print()
obj.display()