from queue import Queue
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
        # recursive calls navigate the tree, no loops required
        # check if node exists
        # if self is None:
        # return False
        # return true if value of node is same as target
        if target == self.value: 
            # base case (returning concrete answer)
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
            # base case (returning concrete answer)
            return False 


    # Return the maximum value found in the tree
    # can improve this by removing line 85, could aslo return self.vale on 75 instead of in a variable
    def get_max(self):
        # store given value
        max_val = self.value
        # store hieght
        tree_height = 0
        
        # check right code if exists
        if not self.right:
            return max_val
        else:
            tree_height += 1
            # update value
            # repeat
            return self.right.get_max()
        # break when no right child exists
        # return max_val

        return max_val
    
    # depth first?
    def iterative_get_max(self):
        current_max = self.value

        current = self

        # traverse 
        while current is not None:
            if current.value > current_max:
                # updates value
                current_max = current.value
            # iterates to next right node if current value is equal or less than current max
            current = current.right


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # depth first?
    def iterate_for_each(self, fn):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)            
            if current.right:
                stack.append(current.left)
            
            fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # use recursion
        # get values
        # stores values
        # get low
        # sort values low - high
        if node.left:
            node.in_order_print(node.left)
        print(str(node.value))
        if node.right:
            node.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # we need to utilize a queue and set it to a var
        storage = Queue()
        # add root to the Q
        storage.enqueue(self)
        # while Q is not empty:
        while (len(storage) > 0):
            # dequeue our node in order to remove from front of line and print it
            remove_item = storage.dequeue()
            # dq method returns the value of our first item in the Q
            print(remove_item.value)
            # check the nodes left and put it in line to be dequed and printed
            if node.left:
                storage.enqueue(node.left)
            # check the nodes right and put it in line to be dequed and printed
            if node.right:
                storage.enqueue(node.right)


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


# comments should be focussed on intent and outcome
# code itself should be telling the story
    # semantic variables