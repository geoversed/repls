# Definition of the Linear Queue class
class LQ:
    # Constructor to initialize an empty Linear Queue
    def __init__(self):
        # List to store elements in the queue
        self.items = []

    # Method to check if the Linear Queue is empty
    def isEmpty(self):
        return self.items == []

    # Method to enqueue an element at the end of the Linear Queue
    def enqueue(self, value):
        # Append the value to the end of the queue
        self.items.append(value)
        # Return a message indicating the successful insertion
        return f"Inserted {value} at the end of the queue."

    # Method to dequeue an element from the front of the Linear Queue
    def dequeue(self):
        # Check if the queue is empty before dequeuing
        if self.isEmpty():
            return "Queue is empty."
        # Remove and return the element from the front of the queue
        return self.items.pop(0)

    # Method to peek at the element at the front of the Linear Queue without dequeuing
    def peek(self):
        # Check if the queue is empty before peeking
        if self.isEmpty():
            return "Queue is empty."
        # Return the element at the front of the queue
        return self.items[0]

    # Method to delete all elements in the Linear Queue
    def delete(self):
        # Check if the queue is empty before deleting
        if self.isEmpty():
            return "Queue is empty."
        # Clear the list to delete all elements in the queue
        self.items = []
        # Return a message indicating the queue is deleted
        return "Queue is deleted."

    # Method to find the index of a specific value in the Linear Queue
    def index(self, value):
        # Return the index of the specified value in the queue
        return self.items.index(value)
