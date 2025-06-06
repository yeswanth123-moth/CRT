class Graph:
    def __init__(self,size):
            self.graph = {}
    def insert_list(self,v,e):
        if v not in self.graph:
            self.graph[v] = [e]
        else:
            self.graph[v].append(e)

    def bfs(self,start):
        queue = [start]
        visited = []
        while queue:
            cur = queue.pop(0) #if 0 it is bfs, without 0 dfs
            if cur not in visited:
                visited.append(cur)
                queue.extend(self.graph[cur])
        print(visited)
obj = Graph()
obj.insert_list("B","T")
obj.insert_list("T","B")
obj.insert_list("B","P")
obj.insert_list("P","B")
obj.insert_list("B","D")
obj.insert_list("D","B")
obj.insert_list("P","D")
obj.insert_list("D","P")
obj.insert_list("T","D")
obj.insert_list("D","T")
obj.insert_list("D","G")
obj.insert_list("G","D")
obj.insert_list("D","K")
obj.insert_list("K","D")
obj.insert_list("K","L")
obj.insert_list("L","K")
print(obj.graph)
obj.bfs("B")