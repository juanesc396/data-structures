class BinarySearchTreeNode:
    # Node Class
    def _init_(self, data):
        self.left = self.right = None
        self.data = data


class BinarySearchTree:
    #Binary Search Tree Class
    def _init_(self):
        """
        Initialize the Binary Search Tree
        """
        self.root = None

    def insert(self, new_data):
        """
        Function to insert a value in the Binary Search Tree
        """
        new_node = BinarySearchTreeNode(new_data)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while current:
            if new_data > current.data and not current.right:
                current.right = new_node
                return
            elif new_data < current.data and not current.left:
                current.left = new_node
                return
            elif new_data == current.data:
                return
            elif new_data > current.data and current.right:
                current = current.right
            elif new_data < current.data and current.left:
                current = current.left
                

    def min_value(self):
        """
        Function that return the minimum value
        """
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def _min_node(self, node):
        """
        Function to extract the node with the minimum value
        """
        min_value = node
        while min_value.left:
            min_value = min_value.left
        return min_value

    def max_value(self):
        """
        Function that return the maximum value into the Binary Search Tree
        """
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def delete_node(self, value):
        """
        Function to delete a node.
        """
        if not self.root:
            return

        prev = None
        current = self.root
        while current and current.data != value:
            prev = current
            if current.data < value:
                current = current.right
            else:
                current = current.left
        if not current:
            return self.root

        elif not current.left and not current.right:
            if prev.right == current:
                prev.right = None
            else:
                prev.left = None

        elif current.right and current.left:
            min_value = self._min_node(current)
            min_value.right = current.right
            min_value.left = current.left
            current = min_value

            if prev:
                if prev.data < min_value.data:
                    prev.right = min_value
                else:
                    prev.left = min_value

        else:
            if current.right:
                current = current.right
            else:
                current = current.left
            if prev:
                if prev.data < current.data:
                    prev.right = current
                else:
                    prev.left = current
            else:
                self.root = current

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data)
            self._inorder(root.right)
    
    def inorder(self):
        """
        Function that traverse the Search Binary Tree with the InOrder method.
        """
        current = self.root
        return self._inorder(current)

    def _preorder(self, root):
        if root:
            print(root.data)
            self._preorder(root.left)
            self._preorder(root.right)

    def preorder(self):
        """
        Function that traverse the Search Binary Tree with the PreOrder method.
        """
        current = self.root
        self._preorder(current)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data)

    def postorder(self):
        """
        Function that traverse the Search Binary Tree with the PostOrder method.
        """
        current = self.root
        self._postorder(current)
