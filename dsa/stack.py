class stack:
    def __init__(self,size):
        self.size = size
        self.box = [0]*self.size
        self.top = -1
    def push(self,data):
        if self.top+1 == self.size:
            print("overflow")
            return
        self.top+=1
        self.box[ self.top ] = data
    def display(self):
        if self.top == -1:
            print("underflow")
            return
        for i in range(self.top,-1,-1):
            print(self.box[i],end=" ")
    def pop(self):
        if self.top == -1:
            print("underflow")
            return
        self.top-=1
    def peek(self):
        if self.top == -1:
            print("underflow")
            return
        print(self.box[self.top])
stack1 = stack(3)
stack1.push(18)
stack1.push(7)
stack1.display()
stack1.pop()
stack1.pop()
print()
stack1.display()