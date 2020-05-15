"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import DoublyLinkedList from doubly_linked_list_copy


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new is < node.value
        if value < self.value:
            # If left doesn't exist, this is the end of the branch.
            if self.left is None:  # Or if not self.left
                # Create a left tree Node...
                self.left = BinarySearchTree(value)
            else:
                # Can't put new node, keep checking.
                self.left.insert(value)
        # Value is >= value
        else:
            # If right doesn't exist, this is the end of the branch.
            if self.right is None:
                # Create a right tree Node...
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value = target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # If there is a value to the right
        if self.right:
            # return a get_max on right
            return self.right.get_max()
        else:
            # Otherwise return the current value.
            return self.value

    # Call the function `fn` on the value of each node
    # Considered a pre-order depth first traversal.
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        if node is None:
            return
        q = DoublyLinkedList(node)

        while q.length > 0:
            print("{}".format(q.head.value.value))
            removed_node = q.remove_from_head()

            if removed_node.left is not None:
                q.add_to_tail(removed_node.left)
            if removed_node.right is not None:
                q.add_to_tail(removed_node.right)

        q.add_to_head(node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        pass

    # * Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        pass
