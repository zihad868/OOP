class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return 'Stack is Empty'

    def stack_empty(self):
        return self.stack == 0

    def display(self):
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0  # Checks if the stack is empty


stack = Stack()
stack.push(45)
stack.push(2)


print(stack.display())  # Output: [45, 2]
print(stack.pop())  # Output: 2 (pops the last element)
print(stack.display())  # Output: [45]
print(stack.stack_empty())