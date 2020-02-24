from NodeB import NodeB
class BinaryTree:
    def __init__(self):
        self.root=None


    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root == None):
            self.root = NodeB(val)
        else:
            self._add(val, self.root)

    def insertleft(self,val):
        newNode=self.root
        n=NodeB(val)
        if (newNode == None):
            self.root = NodeB(val)
        if(newNode.left is None):
            n.left=newNode.left
            self.left=n

    def insetright(self,data):
        newnode = BinaryTree(data)
        if (self.right is None):
            self.root = newnode
        else:
            newnode.right = self.right
            self.right = newnode
    def preorderRecursive(self, result):
        if(not self.root):
            return
        result.append(self.root.data)
        self.preorderRecursive(self.left, result)
        self.preorderRecursive(self.right, result)



