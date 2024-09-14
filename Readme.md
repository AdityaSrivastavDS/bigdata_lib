# BigDataLib

**BigDataLib** is a Python library that provides direct implementations of various big data structures, allowing you to work with these structures efficiently using simple functions. This library includes support for graphs, trees, and more.

## Features

- **Adjacency Matrix**: Efficient representation and manipulation of graph edges.
- **Adjacency List**: Lightweight representation of graph edges with fast access.
- **Trie (Prefix Tree)**: Fast prefix-based search and insertion for strings.
- **Segment Tree**: Efficient range queries and updates.
- **Fenwick Tree (Binary Indexed Tree)**: Fast updates and prefix sum queries.
- **Red-Black Tree**: Self-balancing binary search tree with efficient insertions and deletions.
- **AVL Tree**: Self-balancing binary search tree maintaining height balance.
- **Skip List**: Probabilistic data structure for fast search, insertion, and deletion.
- **B-Tree**: Balanced tree used for efficient data retrieval in databases.
- **B+ Tree**: Similar to B-Tree but with all values stored in leaf nodes.

## Installation

You can install the library using pip:

```bash
pip install bigdata_lib
```

# Usage

## 1.Adjacency Matrix
The adjacency matrix is a 2D array used to represent graph edges. It is memory-intensive but straightforward.
```bash
from bigdata_lib.adjacency_matrix import create_adjacency_matrix, add_edge_matrix, display_matrix

matrix = create_adjacency_matrix(5)
add_edge_matrix(matrix, 1, 2)
display_matrix(matrix)
```

## 2.Adjacency List
The adjacency list is a dictionary where keys are nodes and values are lists of adjacent nodes.
```bash
from bigdata_lib.adjacency_list import add_edge_list, display_list

graph = {}
add_edge_list(graph, 1, 2)
display_list(graph)
```
## 3.Trie (Prefix Tree)
A trie is a tree used for storing strings in a way that allows for fast retrieval of prefixes.
```bash
from bigdata_lib.trie_structure import Trie, TrieNode

trie = Trie()
trie.insert("example")
print(trie.search("example"))  # Output: True
print(trie.search("test"))     # Output: False
```

## 4.Segment Tree
A segment tree is used for storing intervals or segments, allowing efficient querying and updating.
```bash
from bigdata_lib.segment_tree import SegmentTree

arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)
print(segment_tree.query(1, 3))  # Output: 15
segment_tree.update(1, 10)
print(segment_tree.query(1, 3))  # Output: 22
```

## 5.Fenwick Tree (Binary Indexed Tree)
A Fenwick Tree is used for efficient range queries and updates.
```bash
from bigdata_lib.fenwick_tree import FenwickTree

arr = [1, 3, 5, 7, 9, 11]
fenwick_tree = FenwickTree(arr)
print(fenwick_tree.query(3))  # Output: 16
fenwick_tree.update(1, 10)
print(fenwick_tree.query(3))  # Output: 26
```

## 6.Red-Black Tree
A Red-Black Tree is a self-balancing binary search tree with specific rules to ensure balanced height.
```bash
from bigdata_lib.red_black_tree import RedBlackTree

rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(15)
# Implement traversal or other operations as needed
```

## 7.AVL Tree
An AVL Tree is a self-balancing binary search tree where the height difference between left and right subtrees is maintained.
```bash
from bigdata_lib.avl_tree import AVLTree

avl_tree = AVLTree()
root = None
root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 15)
# Implement traversal or other operations as needed
```

## 8.Skip List
A Skip List is a probabilistic data structure that allows fast search, insertion, and deletion operations.
```bash
from bigdata_lib.skip_list import SkipList

skip_list = SkipList(max_level=3, p=0.5)
skip_list.insert(3)
skip_list.insert(6)
skip_list.insert(7)
print(skip_list.search(6))  # Output: True
print(skip_list.search(4))  # Output: False
```

## 9.B-Tree
A B-Tree is a balanced tree used for efficient data retrieval and insertion, often used in database systems.
```bash
from bigdata_lib.b_tree import BTree

b_tree = BTree(t=2)
b_tree.insert(10)
b_tree.insert(20)
b_tree.insert(5)
# Implement traversal or other operations as needed
```

## 10.B+ Tree
A B+ Tree is similar to a B-Tree but with all values stored in leaf nodes, allowing efficient range queries.
```bash
from bigdata_lib.bplus_tree import BPlusTree

bplus_tree = BPlusTree(t=2)
bplus_tree.insert(10)
bplus_tree.insert(20)
bplus_tree.insert(5)
# Implement traversal or other operations as needed
```

# Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
