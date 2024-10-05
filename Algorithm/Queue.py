class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return 'Queue is Empty'

    def display(self):
        return self.queue

    def is_empty(self):
        # This method checks if the queue is empty
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(8)
queue.enqueue(10)
queue.dequeue()  # Removes 8 from the queue
queue.enqueue(52)
print(queue.display())  # Output: [10]