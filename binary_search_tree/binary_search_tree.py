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


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Chack if empty
        # if empty:
        #     Put node here at root
        # elif new < node.value:
        #     leftnode.insert value
        # elif new >= node.value:
        #     rightnode.insert value
        if self.value is None:
            self.value is BinarySearchTree(value)

        else:
            if value < self.value:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)

            else:
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if node is none:
        #     return false
        # if node.value == find value:
        #     return True
        # else:
        #     if find < node.value:
        #             find on left node
        #     else:
        #             find on right node
        if self.value is target:
            return True
        else:
            if target < self.value:
                # This is the Truthy break case for the recursion.
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if node to right exists:
        #     get_max on right
        # else:
        #     return node.value
        if not self.value:
            # Accounting if it's empty
            return
        else:
            if self.right is None:
                # The Break case if there is not a value to the right.
                return self.value
            else:
                return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self.value:
            return
        else:
            # Applies the function to the node.
            fn(self.value)

            # If there is a left value, run the for_each passing in the function.
            if self.left:
                self.left.for_each(fn)

            # If there is a right value, run the for_each passing in the function.
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # Starts at parent
        # Checks left if left exists
        # Checks right if right exists
        height = self.height(node)
        for i in range(1, height+1):
            self.print_level(node, i)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height+1
            else:
                return right_height+1

    def print_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.value)
        elif level > 1:
            node.print_level(node.left, level-1)
            node.print_level(node.right, level-1)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node:
            print(node.value)
            self.dft_print(node.left)
            self.dft_print(node.right)

    # * Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
