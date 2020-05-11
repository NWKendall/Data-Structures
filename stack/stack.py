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



class Stack:
    def __init__(self):
        self.size = 0
        self.total = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def size_of_stack(self):
        self.size = len(self.storage)
        return self.size

    def push(self, value):
        self.total += value
        self.storage.append(value)

    def pop(self):
        if len(self.storage) < 1:
            return None 
        else:
            return self.storage.pop()

stack = Stack()

stack.push(2)
stack.push(4)
stack.push(4)
stack.push(2)
# stack.pop()

print('Storage:', stack.storage)
print('Total:', stack.total)
print('Size:', stack.size_of_stack())











# class Node:
#     def __init__(self, value=None, next_node = None):
#         self.value = value
#         self.next_node = next_node
        
#     def get_value(self):
#         return self.value
    
#     def get_next(self):
#         return self.next_node
    
#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self, head=None):
#         # first node in list
#         self.head = head
        
#     def add(self, value):
#         #regardless, need to wrap value in new node
#         new_node = Node(value)
        
#         # what if the list is empty
#         if not self.head:
#             self.head = new_node
        
#         # what if list is not empty
#         else:
#             # set the new node as next node
#             current = self.head
#             while current.get_next() is not None:
#                 current = current.get_next()
#             current.set_next(new_node)
        

# ll = Node(1)
# ll.next_node = Node(2)
# ll.next_node.next_node = Node(3)
# ll.next_node.next_node.next_node = Node(4)