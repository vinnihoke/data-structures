"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# LIFO


class Stack:
    def __init__(self, storage=None):
        self.size = 0
        self.storage = [] if storage == None else storage

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        self.size -= 1
        if len(self.storage) == 0:
            return None
        else:
            item = self.storage.pop()
            return item


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    # Beg
    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
            self.tail = new_node

    # Beg
    def pop(self):
        self.size -= 1
        if not self.head:
            return None
        else:
            value = self.head
            for i in range(self.size):
                value = value.get_next()
            self.tail = value.get_value()
            if self.tail == self.head.get_value():
                lastValue = self.head
                self.head = None
                return lastValue.get_value()
            return value.get_value()


test = Stack()


print(test.head)
test.push(1)
print(test.head)
test.push(2)
print(test.head)
test.push(3)
print(test.head)
print(test.pop())
print(test.pop())
print(test.pop())
