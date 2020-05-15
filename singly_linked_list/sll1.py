class Node:
    def __init__(self, value=None, next_node=None):
        # The value at this linked list node starts as None
        self.value = value

        # Reference for the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new):
        self.next_node = new


class LL:
    def __init__(self):
        # Reference to the head of the list
        self.head = None

        # Reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # Create a new node with the incoming value
        new_node = Node(value, None)

        # Check if there is no head (List is empty)
        # This is the first iteration creating the Linked List.
        # HT
        # 1
        if not self.head:
            self.head = new_node
            self.tail = new_node

        # Nodes already exist, add to the tail
        else:
            # Grab the tail, call set next, and pass in the new_node
            self.tail.set_next(new_node)

            # Set the tail to the new node
            # This is the second iteration in my drawings.
            # H     T
            # 1     2
            self.tail = new_node

    def remove_head(self):
        # Return none if there is no head. List is empty.
        if not self.head:
            return None

        # If head has no next then it's the only node in the list
        if not self.head.get_next():

            # Store a reference for the current head
            head = self.head

            # Delete the lists head reference by alienating it.
            self.head = None

            # Because there is no head, and this was the only thing in our list, we also need to clear our tail.
            # This resets the list back to empty.
            self.tail = None

        else:
            # There are more than one items in the list
            # Create a reference to the current head value.
            value = self.head.get_value()

            # Set the head reference to the current heads next node.
            self.head = self.head.get_next()

            # Return the value for the removed head.
            return value

    def remove_tail(self):
        # Return none if there is no head. List is empty.
        if not self.head:
            return False

        # This means there is only one node in the list.
        if self.head is self.tail:
            # Create a reference to the current value of the head.
            value = self.head.get_value()

            # Reset the LL back to empty
            self.head = None
            self.tail = None

            # Return the head value
            return value

        # Create a reference for the current node
        current = self.head

        # ? Traverse the list setting current each time.
        # Check if we're at a valid node.
        while current.get_next() is not self.tail:

            # Set current to the next node's reference.
            # This is checking for a valid get_next, if it is the tail, it'll break.
            # Current will now be the value right before the tail.
            current = current.get_next()

        # Store a reference to the current tail's value
        value = self.tail.get_value()

        # Set the tail to the value right before the current tail. Alienating the tail, and removing it.
        self.tail = current

        # Return the deleted value
        return value

    def search(self, value):
        # If list is empty return false. Can't search an empty list.
        if not self.head:
            return False

        #  Get a reference to our current head.
        current = self.head

        # Check if we're at a valid node.
        while current:
            # Return True if the value matches the current.get_value()
            if current.get_value() == value:
                return True

            #  Update current node to the current node's next node
            current = current.get_next()

        # If it hasn't been returned above, it isn't in our list. Return False.
        return False

    def get_max(self):
        # If list is empty return false. Max is zero technically.
        if not self.head:
            return None

        # Create a reference for the largest value we've seen so far. first value.
        max = self.head.get_value()

        # Create a reference for our current node as we traverse the list.
        current = self.head.get_next()

        # Check to see if we're at a valid node
        while current:
            # Is current value greater than the max?
            if current.get_value() > max:
                # Set it to max
                max = current.get_value()

            # Update the current node to the next node in the list
            current = currne.get_next()

        # If we arrive here we should have the max value stored. Return max.
        return max

        # Store a reference to the node we're currently at and update it as we traverse the list.
        current = self.head

        # Iterate over the next values to check if we're at a valid node
        while current:
            # Return True if the current value matches the target
