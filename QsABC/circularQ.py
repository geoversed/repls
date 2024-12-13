# Definition of the Circular Queue class
class CQueue:
    # Constructor to initialize the Circular Queue with a given capacity (k)
    def __init__(self, k):
        # Creating list represent CQ with 'k' elements, initialized to None
        self.queue = [None] * k
        # Capacity of the Circular Queue
        self.k = k
        # Front and rear pointers initially set to -1 to indicate an empty queue
        self.front = -1
        self.rear = -1
        # Size of the Circular Queue
        self.size = 0

    # Method to enqueue an element into the Circular Queue
    def enQueue(self, val):
        # Check if the queue is full before enqueuing
        if self.size == self.k:
            return
        # Move the rear pointer to the next position (circular increment)
        self.rear = (self.rear + 1) % self.k
        # Set the value at the rear position in the queue
        self.queue[self.rear] = val
        # Increment the size of the queue
        self.size += 1
        # Update the front pointer if it is the first element in the queue
        if self.front == -1:
            self.front = self.rear

    # Method to dequeue an element from the Circular Queue
    def deQueue(self):
        # Check if the queue is empty before dequeuing
        if self.size == 0:
            return
        # Retrieve the value from the front position in the queue
        val = self.queue[self.front]
        # Move the front pointer to the next position (circular increment)
        self.front = (self.front + 1) % self.k
        # Decrement the size of the queue
        self.size -= 1
        # Return the dequeued value
        return val

    # Method to get the value at the front of the Circular Queue without dequeuing
    def Front(self):
        if self.size == 0:
            return -1
        return self.queue[self.front]

    # Method to get the value at the rear of the Circular Queue without dequeuing
    def Rear(self):
        if self.size == 0:
            return -1
        return self.queue[self.rear]

    # Method to check if the Circular Queue is empty
    def isEmpty(self):
        return self.size == 0

    # Method to check if the Circular Queue is full
    def isFull(self):
        return self.size == self.k

    # Method to print the elements of the Circular Queue
    def printQueue(self):
        # Check if the queue is empty
        if self.size == 0:
            print("Empty Queue")
            return
        # Print the elements of the Circular Queue
        print("", end="")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()