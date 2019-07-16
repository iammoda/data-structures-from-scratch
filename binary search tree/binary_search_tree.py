class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, curr, traversal):
        if curr:
            traversal += curr.val + "-"
            traversal = self.preorder(curr.left, traversal)
            traversal = self.preorder(curr.left, traversal)
        print traversal

    def postorder(self, curr, traversal):
        if curr:
            traversal = self.postorder(curr.left, traversal)
            traversal = self.postorder(curr.right, traversal)
            traversal += curr.val + "-"
        print traversal

    def inorder(self, curr, traversal):
        if curr:
            traversal = self.postorder(curr.left, traversal)
            traversal += curr.val + "-"
            traversal = self.postorder(curr.right, traversal)
        print traversal

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, curr, data):
        if data > curr.data:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert(data, curr.left)

        elif data < curr.data:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(data, curr.right)

        else:
            print "value already present"

    def find(self, data):
        if self.root:
            found = self._find(data, self.root)
            if found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, curr, data):
        if data > curr.data and curr.right:
            return self._find(data, curr.right)
        elif data < curr.data and curr.left:
            return self._find(data, curr.left)
        elif data == curr.data:
            return True




