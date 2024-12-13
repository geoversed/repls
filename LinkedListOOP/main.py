"""RR6-23AhmedS Linked List Creation via OOP"""


"""
Currently available operations: prepend, insert_in_order, traverse list,
delete node from list, 
"""



class Node():
    """A class for a node in the linked list"""

    def __init__(self, given_data):
        """Constructor method for the Node class"""
        self.data = given_data
        self.next = None

    def get_data(self):
        """Retrieves data at a given point. this is a getter method"""
        return self.data

    def get_next(self):
        """Retrieves the item next to the current item. this is also a getter method."""
        return self.next

    def set_next(self, new_next):
        """Modifies the next item in the node. this is a setter method"""
        self.next = new_next


class LinkedList():
    """A class for the linked list"""

    def __init__(self):
        """Constructor method"""
        self.head = None # Initialise to None as the linked list is empty

    def get_head(self):
        """Retrieves head of the linked list (starting node). this is a getter method"""
        return self.head

    def set_head(self, new_head):
        """Modifies head of the linked list. this is a setter method"""
        self.head = new_head

    def prepend(self, data):
        """Insert a node to the front of the list"""

        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.get_head() is None:
            self.set_head(new_node)
        else:
            # Update the pointers so the new node is the head
            new_node.set_next(self.get_head())            
            self.set_head(new_node)

    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""

        # Create a new node
        new_node = Node(data)

        # Start at the head of the list
        current = self.get_head()

        # Check if there are no nodes in the list
        if current is None:
            self.set_head(new_node)

        # Check if the new node data is before the head data
        elif new_node.get_data() < current.get_data():
            # Set the new node as the head of the list
            new_node.set_next(self.get_head())
            self.set_head(new_node)

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.get_next() is not None
                  and current.get_next().get_data() < new_node.get_data()):
                # Get the next node
                current = current.get_next()

            # Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)

    def traverse(self):
        """Traverse the list and output the data from each node"""

        # Set the current node as the head
        current = self.get_head()

        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()
  
    def delete(self, data):
        """Delete a node. Checks if the node exists as well."""

        # Start at the head of the list
        current = self.get_head()

        # Check if the head node is to be deleted
        if current.get_data() == data:
            # Update the head pointer
            self.set_head(current.get_next())
        else:
            # Repeat until the node has been found
            while current.get_next() is not None and current.get_next().get_data() != data:
                # Change the current node to be the next node
                current = current.get_next()

            # Set the pointer to be the next node's pointer.
            # Also checks if list isnt empty before accessing its attributes.
            if current.get_next() is not None:
              current.set_next(current.get_next().get_next())

    def pop_first(self):
      """Delete the first node in the linked list"""
      # Check if the list is empty
      if self.get_head() is None:
          print("The list is empty. Cannot pop the first element.")
          return

      # Update the head pointer to the next node
      self.set_head(self.get_head().get_next())

    def pop(self):
      """Delete the last node in the linked list"""
      # Check if the list is empty
      if self.get_head() is None:
          print("The list is empty. Cannot pop the last element.")
          return

      # Start at the head of the list
      current = self.get_head()

      # Check if there is only one node in the list
      if current.get_next() is None:
          self.set_head(None)
          return

      # Repeat until the last node is reached
      while current.get_next().get_next() is not None:
          current = current.get_next()

      # Set the next pointer of the second-to-last node to None
      current.set_next(None)

    def delete_all(self):
      """Delete all nodes in the linked list"""
      # Set the head pointer to None, effectively emptying the list
      self.set_head(None)


def insert_test_data(my_list):
    """"Insert test data into the linked list"""

    my_list.insert_in_order("Berth")
    my_list.insert_in_order("Maya")
    my_list.insert_in_order("Zara")  # These values are stored in order
    my_list.insert_in_order("Mina")
    my_list.insert_in_order("George")


def main():
    """Create a linked list and insert, delete and traverse the list"""
    print("### Linked list (OOP) ###")

  
    # Instantiate an empty linked list object
    my_list = LinkedList()

  
    # Insert test data into the linked list
    print("\nInsert test data into the linked list in order:")
    insert_test_data(my_list)
    my_list.traverse()  # traverse through the list in order when needed

  
    # Testing - insert at front
    print("\nInsert a node named Zihan to the front of the list:")
    my_list.prepend("Zihan") # Zihan becomes the head
    my_list.traverse()

  
    # Testing - insert in order
    print("\nInsert a node named Zeeba to the end of the list:")
    my_list.insert_in_order("Zeeba")  # Zeeba is inserted + ordered
    my_list.traverse()

  
    # Testing - delete a node
    print("\nDelete a node named Zara from the list:")
    my_list.delete("Zara")  # Zara is removed, if she exists
    my_list.traverse()

  
    # Testing - delete the first node
    print("\nDelete the first node in the list:")
    my_list.pop_first()
    my_list.traverse()

  
    # Testing - delete the last node
    print("\nDelete the last node in the list:")
    my_list.pop()
    my_list.traverse()

  
    # Testing - delete all nodes
    print("\nDelete all nodes in the list:")
    my_list.delete_all()
    my_list.traverse()  # The list should be empty


main()