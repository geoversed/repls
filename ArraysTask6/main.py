from typing import Any, Optional, Union


class BinaryTree:
    """
    Represents a Binary Tree data structure 
    available with left-order traversal 
    and other common operations.
    """

    def __init__(self, data: Optional[Any] = None):
        # Initialize the Binary Tree node with data, left child, and right child
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_node(self, rootNode, nodeValue) -> str:
        # Insert a new node with the given value into the binary tree
        if not rootNode.data:
            # If the root node does not have data, set the data to the given value
            rootNode.data = nodeValue

        # Determine which child (left or right) the new node should be inserted into
        is_less_check = nodeValue <= rootNode.data
        which_child = rootNode.left_child if is_less_check else rootNode.right_child

        if not which_child:
            # If the child node does not exist, create a new node and set it as the child
            setattr(rootNode, 'left_child' if is_less_check else 'right_child', BinaryTree(nodeValue))
        else:
            # If the child node exists, recursively insert the new node into the child node
            self.insert_node(which_child, nodeValue)

        return "Node inserted successfully."

    def pre_order_traversal(self, rootNode) -> Union[None, Any]:
      # Perform a pre-order traversal of the binary tree starting from the root node
      if not rootNode:
        # If the root node is empty, return None
        return

      # Print the data of the current node and traverse the left and right children recursively
      print(rootNode.data)
      self.pre_order_traversal(rootNode.left_child)
      self.pre_order_traversal(rootNode.right_child)

    def in_order_traversal(self, rootNode) -> Union[None, Any]:
      # Perform an in-order traversal of the binary tree starting from the root node
      if not rootNode:
        return
      self.in_order_traversal(rootNode.left_child)
      print(rootNode.data)
      self.in_order_traversal(rootNode.right_child)
    
    def post_order_traversal(self, rootNode) -> Union[None, Any]:
      # Perform a post-order traversal of the binary tree starting from the root node
      if not rootNode:
        return
      self.post_order_traversal(rootNode.left_child)
      self.post_order_traversal(rootNode.right_child)
      print(rootNode.data)

# Create an instance of the Binary Tree
new_binary_tree = BinaryTree()
new_binary_tree.insert_node(new_binary_tree, 80)
new_binary_tree.insert_node(new_binary_tree, 50)
new_binary_tree.insert_node(new_binary_tree, 60)
new_binary_tree.insert_node(new_binary_tree, 80)
new_binary_tree.insert_node(new_binary_tree, 90)
new_binary_tree.insert_node(new_binary_tree, 20)
new_binary_tree.insert_node(new_binary_tree, 40)

# Perform pre-order traversal on the binary tree
print("Pre-order traversal:")
print(new_binary_tree.pre_order_traversal(new_binary_tree))

print("-------")

# Perform in-order traversal on the binary tree
print("\nIn-order traversal:")
new_binary_tree.in_order_traversal(new_binary_tree)

print("-------")

# Perform post-order traversal on the binary tree
print("\nPost-order traversal:")
new_binary_tree.post_order_traversal(new_binary_tree)
