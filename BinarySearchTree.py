from BinaryTree import BinaryTree, Node

class BinarySearchTreeEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}: {self.value})"

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
        self.size = 0  # Inicializa el tamaño

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, current, key):
        if current is None:
            return None
        if key == current.data.key:  
            return current
        if key < current.data.key:
            return self._find(current.left, key)
        return self._find(current.right, key)
    
    def find_min(self):
        if self.is_empty():
            return None
        return self._find_min(self.root).data

    def _find_min(self, current):
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        if self.is_empty():
            return None
        return self._find_max(self.root).data

    def _find_max(self, current):
        while current.right is not None:
            current = current.right
        return current
    

    def insert(self, key, value):
        entry = BinarySearchTreeEntry(key, value)
        if self.is_empty():
            self.root = Node(entry)
            self.size = 1
        else:
            self._insert_node(self.root, entry)

    def _insert_node(self, current, entry):
        if entry.key < current.data.key:
            if current.left is None:
                current.left = Node(entry)
                self.size += 1
            else:
                self._insert_node(current.left, entry)
        else:
            if current.right is None:
                current.right = Node(entry)
                self.size += 1
            else:
                self._insert_node(current.right, entry)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data.key)
            self._inorder_recursive(node.right, result)

    def _remove(self, current, key):
        if current is None:
            return current

        if key < current.data.key:
            current.left = self._remove(current.left, key)
        elif key > current.data.key:
            current.right = self._remove(current.right, key)
        else:
            if current.left is None:
                self.size -= 1
                return current.right
            elif current.right is None:
                self.size -= 1
                return current.left

            temp = self._find_min(current.right)
            current.data = temp.data
            current.right = self._remove(current.right, temp.data.key)
        return current

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _find_min(self, current):
        while current.left is not None:
            current = current.left
        return current
    
class BinarySearchTreeEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}: {self.value})"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
