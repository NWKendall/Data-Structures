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
        # check if empty
        if self is None:
            self = BinarySearchTree(value)
        # if populated
        
        # check value of new node
        # if smaller add to self.left
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
        # self.value >= value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if node exists
        # if self is None:
        #     return False
        # return true if value of node is same as target
        if target == self.value: # base case (returning concrete answer)
            return True
        # if smaller, recursive call on left child 
        elif target < self.value:
            # check to see if lef child exists on current child
            if self.left:
                # if true, recusrive call on left child
                return self.left.contains(target)
        # if larger, recursive call on right child 
        elif target > self.value:
            # check to see if lef child exists on current child
            if self.right:
                # if true, recusrive call on left child
                return self.right.contains(target)
        else:
            # should this False return be in each child check? 
            return False # base case (returning concrete answer)


    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
