def print_tree_in_order(node, level=0):
    if node is not None:
        if not node.leaf:
            for i in range(len(node.keys)):
                print_tree_in_order(node.children[i], level + 1)
                print(' ' * 4 * level + '->', node.keys[i])
            print_tree_in_order(node.children[len(node.keys)], level + 1)
        else:
            print(' ' * 4 * level + '->', node.keys)
