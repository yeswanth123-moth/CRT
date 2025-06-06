class Node:
    def __init__(self,data):
        self.data=data     #data for the node 
        self.left=None     #value stored in left side
        self.right=None    #value stored in right side
        
class binary_tree:  #new class created
    
        
    def inorder_traversal(self,root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.data,end=" ")
        self.inorder_traversal(root.right)

    def height(self,root):  #finding height of the tree
        if root is None or root.left is None and root.right is None:
            return 0
        l_count=1+self.height(root.left)
        r_count=1+self.height(root.right)
        return l_count if l_count>r_count else r_count    

root=Node(5)
root.left=Node(6)
root.right=Node(12)
root.right.right=Node(3)
root.left.left=Node(10)
root.left.right=Node(33)
root.left.left.left=Node(56)
obj=binary_tree()
obj.inorder_traversal(root)
print()
print(obj.height(root)) 