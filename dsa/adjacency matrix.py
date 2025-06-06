class Graph:
    def __init__(self,size):
        self.graph = [ [0]*size for i in range(size)]
        self.dict = {"B": 0, "T": 1, "P": 2, "D": 3, "L": 4}
    def insert_list(self,v,e):
        if v not in self.graph:
            self.graph[v] = [e]
        else:
            self.graph[v].append(e)

    def insert_matrix(self,v,e):
        row , col = self.dict[v] ,self.dict[e]
        self.graph[row][col]=1
        self.graph[col][row]=1
obj = Graph(5)
obj.insert_matrix("B","T")
obj.insert_matrix("B","P")
obj.insert_matrix("B","L")
obj.insert_matrix("D","P")
obj.insert_matrix("D","T")
print(obj.graph)