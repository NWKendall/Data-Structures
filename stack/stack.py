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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        self.storage.pop()

stack = Stack()
stack.push(2)
stack.push(4)

print(stack.storage)











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