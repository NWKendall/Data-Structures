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

# https://www.geeksforgeeks.org/linked-list-vs-array/
# LL
  # Memory storage for LL is more dynamic than arrays.
  # Memory storage for LL is more dynamic than arrays.
  # insertion and deletion are faster
  # require more net memory for functionality
  # memory utilization efficient

# Array
  # arrays are quicker as have set size
  # data is contiguous
  # elements belong to an index
  # insertion and deletion are more intensive
  # memory utilization inefficient


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.total = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def size_of_stack(self):
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         self.total += value
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) < 1:
#             return None
#         else:
#             return self.storage.pop()

# stack = Stack()

# stack.push(2)
# stack.push(4)
# stack.push(4)
# stack.push(2)
# stack.pop()

# print('Stack Storage:', stack.storage)
# print('Stack Total:', stack.total)
# print('Stack Size:', stack.size_of_stack())


# for each node
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



class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        self.tail = None
    
    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)

        # what if the list is empty?
        if not self.head:
            self.head = new_node
        
        if self.tail:
            self.tail.next_node = new_node

        self.tail = new_node
        
        # # what if the list isn't empty?
        # else:
        #     # what node do we want to add the new node to?
        #     # the last node in the list
        #     # we can get to the last node in the list by traversing it
        #     current = self.head
        #     while current.get_next() is not None:
        #         current = current.get_next()
        #     # we're at the end of the linked list
        #     current.set_next(new_node)

    # removes first item in list (head)
        # not good for stacks!
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        elif not self.head.get_next():
            return self.head.get_value()
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value
    
    def remove_last(self):
        # if only one node in list, remove it
        node = self.head
        # while node has a next, move onto next node
        while not node:
            node = node.next_node

        # if node has no next, remove
            if not node.next_node:
                node = None

class Stack:
    # LIFO!
    def __init__(self):
        # size = len of list
        self.size = 0
        # total =sum of list values
        self.total = 0
        self.storage = LinkedList()

    def __iter__(self):
        node = self.storage.head
        while node:
            node = node.next_node
            print(node.value)

    def get_head(self):
        return self.storage.head.get_value()

    def push(self, value):
        self.size += 1
        self.total += value
        self.storage.add_to_end(value)

    def pop(self):
        if not self.storage:
            return None
        else:
            self.size -= 1
            return self.storage.remove_last()



stack = Stack()
stack.push(10)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.pop()



stack.__iter__()
print("Head:", stack.get_head())
print("Size:", stack.size)
print("Total:", stack.total)
