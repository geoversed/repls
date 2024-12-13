# Importing the abstract data structures
from linearQ import LQ  
from circularQ import CQueue

# Function to create and demonstrate a Linear Queue
def create_linear_queue():
    # Creating an instance of the Linear Queue
    myq = LQ()

    # Enqueueing elements into the Linear Queue
    myq.enqueue("1")
    myq.enqueue("5")
    myq.enqueue("32")
    myq.enqueue("64")

    # Formatting all items in the queue as a string for display
    all_items_str_fmt = " ".join(myq.items)

    # Printing the formatted string of all items in the Linear Queue
    print(all_items_str_fmt)

# Function to create and demonstrate a Circular Queue
def create_circular_queue():
    # Creating an instance of the Circular Queue with a capacity of 10
    myq = CQueue(10)

    # Enqueueing elements into the Circular Queue
    myq.enQueue("t")
    myq.enQueue("a")
    myq.enQueue(5)

    # Printing the Circular Queue
    myq.printQueue()

a = create_linear_queue()
b = create_circular_queue()  
