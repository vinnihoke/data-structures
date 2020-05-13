class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = Node(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = Node(value, current_prev, self)
        if current_prev:
            current_prev = self.prev

    def remove(self):
        if self.prev:
            # Grab the previous and set it's next to the current node's next.
            self.prev.next = self.next
        if self.next:
            # Grab the next and set it's prev to the current node's prev.
            self.next.prev = self.prev


class DLL:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        self.length += 1
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.remove()
        elif node is self.tail:
            self.tail = node.prev
            node.remove()
        else:
            node.remove()

    def get_max(self):
        current = self.head
        max = self.head.value
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max
