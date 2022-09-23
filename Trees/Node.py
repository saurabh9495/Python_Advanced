class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def search(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " Not Found"
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                return str(data) + " Not Found"
            return self.right.search(data)
        else:
            print(str(self.data) + ' is found')

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            minVal = self.right.findMin()
            self.data = minVal
            self.right = self.right.delete(minVal)
        return self
    
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
            
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
        
    def levelorder(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            print(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)
    
    def size(self):
        if self is None:
            return 0
        return 1 + self.left.size() + self.right.size()
    
    def isBST(self):
        if self.left:
            if self.left.data > self.data:
                return False
            else:
                return self.left.isBST()
        if self.right:
            if self.right.data < self.data:
                return False
            else:
                return self.right.isBST()
        return True
    
    def isBalanced(self):
        if self is None:
            return True
        lh = self.height(self.left)
        rh = self.height(self.right)
        if abs(lh - rh) <= 1 and self.left.isBalanced() and self.right.isBalanced():
            return True
        return False