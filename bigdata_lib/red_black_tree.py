class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackTreeNode(None)
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def insert(self, value):
        new_node = RedBlackTreeNode(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert_helper(self.root, new_node)
        self._fix_insert(new_node)

    def _insert_helper(self, root, node):
        if root == self.NIL:
            self.root = node
        elif node.value < root.value:
            if root.left == self.NIL:
                root.left = node
                node.parent = root
            else:
                self._insert_helper(root.left, node)
        else:
            if root.right == self.NIL:
                root.right = node
                node.parent = root
            else:
                self._insert_helper(root.right, node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
