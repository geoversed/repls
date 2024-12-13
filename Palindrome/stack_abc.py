# Definition of the Stack class
class Stack:
    # Constructor to initialize an empty stack
    def __init__(self):
        # List to store elements in the stack
        self.stack = []

    # Method to push an item onto the top of the stack
    def push(self, item):
        # Append the item to the stack
        self.stack.append(item)

    # Method to pop and return the item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # Method to peek at the item on the top of the stack without removing it
    def peek(self):
        return self.stack[-1]

    # Method to get the size (number of elements) of the stack
    def size(self):
        return len(self.stack)

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.size() == 0

    # Method to check if the stack is full (assumed to be full when size is 3)
    def isfull(self):
        return self.size() == 3

    # String representation of the stack for easy printing
    def __str__(self):
        return str(self.stack)

    # Representation of the stack for unambiguous identification
    def __repr__(self):
        return str(self.stack)
