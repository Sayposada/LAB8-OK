class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_root(self, node):
        return node == self.root

    def is_internal(self, node):
        return node.left is not None or node.right is not None

    def has_left(self, node):
        return node.left is not None

    def has_right(self, node):
        return node.right is not None

    def root(self):
        return self.root

    def left(self, node):
        return node.left

    def right(self, node):
        return node.right

    def parent(self, node):
        return self._find_parent(self.root, node)

    def _find_parent(self, current, node):
        if current is None or current == node:
            return None
        if current.left == node or current.right == node:
            return current
        left_parent = self._find_parent(current.left, node)
        if left_parent:
            return left_parent
        return self._find_parent(current.right, node)

    def depth(self, node):
        if node is None:
            return -1
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))

    def height(self, node):
        if node is None:
            return -1
        if node.left is None and node.right is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def add_root(self, data):
        if self.root is not None:
            raise ValueError("Root already exists")
        self.root = Node(data)
        self.size = 1

    def insert_left(self, parent_node, data):
        if parent_node.left is not None:
            raise ValueError("Left child already exists")
        parent_node.left = Node(data)
        self.size += 1

    def insert_right(self, parent_node, data):
        if parent_node.right is not None:
            raise ValueError("Right child already exists")
        parent_node.right = Node(data)
        self.size += 1

    def remove(self, node):
        parent = self.parent(node)
        if parent is None: 
            self.root = None
        elif parent.left == node:
            parent.left = None
        else:
            parent.right = None
        self.size -= 1
        
    def display(self):
        lines = []
        self._display_aux(self.root, "", lines)
        for line in lines:
            print(line)

    def _display_aux(self, node, indent, lines):
        if node is None:
            return

        lines.append(f"{indent}{node.data}")

        if node.left:
            self._display_aux(node.left, indent + "    ", lines)
        else:
            lines.append(f"{indent}    None")

        if node.right:
            self._display_aux(node.right, indent + "    ", lines)
        else:
            lines.append(f"{indent}    None")

