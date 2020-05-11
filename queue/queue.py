"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:
#     def __init__(self, storage=None):
#         self.size = 0
#         self.storage = [] if storage == None else storage

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.insert(0, value)

#     def dequeue(self):
#         self.size -= 1
#         if len(self.storage) == 0:
#             return None
#         else:
#             item = self.storage.pop()
#             print(item)
#             return item

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


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def enqueue(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def dequeue(self):
        self.size -= 1
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


test = Queue()

# test.enqueue(1)
# print(test.storage)
# test.enqueue(2)
# print(test.storage)
# test.enqueue(3)
# print(test.storage)

# test.dequeue()
# print(test.storage)
# test.dequeue()
# print(test.storage)
# test.dequeue()
# print(test.storage)
# test.dequeue()


test.enqueue(1)
print(test.head)
test.enqueue(2)
print(test.head)
test.enqueue(3)
print(test.head)

test.dequeue()
print(test.head)
test.dequeue()
print(test.head)
test.dequeue()
print(test.head)
test.dequeue()
