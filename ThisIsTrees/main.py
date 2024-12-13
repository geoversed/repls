# Define a class representing a tree node
class TreeNode:

  # Constructor initializes the node with data and optional children
  def __init__(self, data, children=[]):
    self.data = data 
    self.children = children

  # String representation of the node, with optional indentation
  def __str__(self, level=0):
    ret = " " * level + str(self.data) + "\n"
    for child in self.children:
      ret += child.__str__(level + 1)
    return ret

  # Method to add a child node to the current node
  def addChild(self, node):
    self.children.append(node)

# Create a tree node representing "Drinks" with no initial children
tree = TreeNode("Drinks", [])

# Create additional nodes representing "Hot" and "Cold"
hot = TreeNode("Hot", [])
cold = TreeNode("Cold", [])

# Add "Hot" and "Cold" as children to the "Drinks" node
tree.addChild(hot)
tree.addChild(cold)

# Print the tree structure
print(tree)

# Create additional nodes representing "Tea," "Coffee," "Cola," and "Fanta"
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])

# Add "Cola" and "Fanta" as children to the "Cold" node
cold.addChild(cola)
cold.addChild(fanta)

# Print the tree structure again with the updated children
print("\n\n")
print("With subtree children")
print(tree)
