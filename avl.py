class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        self.height = 1 
    

class AVL:

    def __init__(self):
        self.root = None

    def insert_aux(self, val):
        self.root = self.insert(self.root, val)
        
    # insert
    def insert(self,node,val):
        if node == None:
            return Node(val)
        
        if val < node.val:
            node.left = self.insert(node.left,val)
        if val > node.val:
            node.right = self.insert(node.right,val)


        node.height = 1 + max(self.height(node.left), self.height(node.right))
        b = self.balance(node)


        if b < -1 and val > node.right.val:
            return self.left_rotate(node)
        if b < -1 and val <node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        if b > 1 and val < node.left.val:
            return self.right_rotate(node.left)
        if b > 1 and val > node.left.val :
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
            
        return node      

    # balance
    def balance(self, node):
        if node == None:
            return 0
        else :
            return (self.height(node.left) - self.height(node.right))

    # height
    def height(self,node):
        if node == None:
            return 0
        else:
            return node.height


    # left-rotate
    def left_rotate(self, node):
        child = node.right
        t = child.left

        child.left = node
        node.right = t 

        child.height = 1 + max(self.height(child.left), self.height(child.right))
        node.height = 1 + max(self.height(node.right), self.height(node.right))

        return child

    # right-rotate
    def right_rotate(self,node):

        child = node.left 
        t = child.right 

        child.right = node 
        node.left = t 

        child.height = 1 + max(self.height(child.left), self.height(child.right))
        node.height = 1 + max(self.height(node.right), self.height(node.right))

        return child 
        


    # inorder-traversal
    def inorder(self, node):
        if node == None:
            return 
        
        self.inorder(node.left)
        print(node.val, end="-")
        self.inorder(node.right) 


avtree = AVL()
avtree.insert_aux(23)
avtree.insert_aux(32)
avtree.insert_aux(8)
avtree.insert_aux(12)
avtree.inorder(avtree.root)

    