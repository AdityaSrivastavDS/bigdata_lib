class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _split_child(self, parent, index):
        t = self.t
        node = parent.children[index]
        new_node = BTreeNode(t, node.leaf)
        parent.children.insert(index + 1, new_node)
        parent.keys.insert(index, node.keys[t - 1])
        new_node.keys = node.keys[t:]
        node.keys = node.keys[:t - 1]
        if not node.leaf:
            new_node.children = node.children[t:]
            node.children = node.children[:t]

    def _insert_non_full(self, node, key):
        if node.leaf:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)
