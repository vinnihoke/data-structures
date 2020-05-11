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


# class Stack:
#     def __init__(self, storage=None):
#         self.size = 0
#         self.storage = [] if storage == None else storage

#     def __len__(self):
#         if self.size < 0:
#             self.size = 0
#         return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         self.size -= 1
#         if len(self.storage) == 0:
#             return None
#         else:
#             item = self.storage.pop()
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
            self.tail = self.head
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
                tail = current
            current.set_next(new_node)

    # Beg
    def pop(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value


test = Stack()


print(test.head)
test.push(1)
print(test.head)
test.push(2)
print(test.head)
test.push(3)
print(test.head)
print(test.pop())  # ! Outputting 1
print(test.pop())  # ! Outputting 2
print(test.pop())  # ! Outputting 3
