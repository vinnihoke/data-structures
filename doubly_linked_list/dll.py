class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        # For the current node, store the next value
        current_next = self.next

        # Create a new Node with self as prev, and current self.next
        self.next = Node(value, self, current_next)

        # If current_next is not None, set current_next.prev to self.next. This advances it up the list.
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        # For the current node, store the prev value
        current_prev = self.prev

        # Create a new Node with self.prev as prev, and current self
        self.prev = Node(value, current_prev, self)

        # If current_prev is not None, set current_prev.next to self.prev. This advances it down the list.
        if current_prev:
            current_prev.next = self.prev

    def remove(self):
        # Links to the values around the node on both sides if a prev or next exist. This would make the current node obsolete.
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DLL:
    def __init__(self, node=None):
        # Accepting a passed in node. Defaults to None
        self.head = node
        self.tail = node
        # Tracking value
        self.length = 1 if node is not None else 0

    # If len() is called on DLL it'll return self.length
    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # Increment length of list
        self.length += 1
        # Create the incoming node, set prev and next to None.
        new_node = Node(value)

        # If the node is new...
        if not self.head and not self.tail:
            # This node is the head and tail
            self.head = new_node
            self.tail = new_node

        # Nodes already exist.
        else:
            # The incoming node.next will be existing self.head.
            new_node.next = self.head
            # The incoming node's next node's prev is now new_node
            # Skip ahead one and link back
            self.head.prev = new_node
            # The incoming node's head is now new_node
            # Link forward one.
            self.head = new_node

    def remove_from_head(self):
        # Record and return the current node's value as part of spec
        value = self.head.value

        # Fire the delete method on the DLL class.
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        # Increment length of list
        self.length += 1
        # Create the incoming node, set prev and next to None.
        new_node = Node(value)

        # If the node is new...
        if not self.head and not self.tail:
            # This node is the head and tail
            self.head = new_node
            self.tail = new_node

        # Nodes already exist.
        else:
            # The incoming node.prev will be existing self.tail.
            new_node.prev = self.tail

            # The previous node's next node's next is now new_node
            # Fall back one and link forward.
            self.tail.next = new_node

            # The incoming node's tail is now new_node
            # Link forward one.
            self.tail = new_node

    def remove_from_tail(self):
        # Record and return the current node's value as part of spec
        value = self.tail.value

        # Fire the delete method on the DLL class.
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        # Skip if it's already the head.
        if node is self.head:
            return

        # Fire add_to_tail with the node.value. This makes self.head and self.tail None, then adds the values needed.
        self.add_to_head(node.value)

        # Node has now been added to the head, and will be deleted. Remove will set the current node's prev and next attributes, making the current node obsolete.
        # Linking around the current node, making it irrelevant.
        self.delete(node)

    def move_to_end(self, node):
        if node is self.tail:
            return
        # Same as above, but fires add_to_tail
        self.add_to_tail(node.value)

        # Linking around the current node, making it irrelevant.
        self.delete(node)

    def delete(self, node):
        self.length -= 1

        # Deleted node is the only value.
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # Deleted node is the self.head
        elif node is self.head:
            # If this is the first value in list, change the head to the next Node in the list.
            self.head = node.next

            # Linking around the current node, making it irrelevant.
            node.remove()

        # Deleted node is the self.tail
        elif node is self.tail:
            # If this is the last value in list, change the tail to the prev Node in the list.
            self.tail = node.prev

            # Linking around the current node, making it irrelevant.
            node.remove()

        else:
            # Linking around the current node, making it irrelevant.
            node.remove()

    def get_max(self):
        # Create a current iterator for while loop
        current = self.head

        # Store/record largest as variable
        max = self.head.value
        # Loop through all nodes
        while current is not None:
            if current.value > max:
                max = current.value
            # This is to advance the loop
            current = current.next
        # Return max
        return max
