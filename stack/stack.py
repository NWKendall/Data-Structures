from sll_no_tail import LinkedList, Node

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
#         return sel.size

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

class Stack:
    # LIFO!
    def __init__(self):
        # size = len of list
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.storage.head
        while node is not None:
            print(node.value)
            node = node.get_next()

    def get_head(self):
        return self.storage.head.get_value()

    def get_tail(self):
        return self.storage.get_tail()

    def push(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)



print("Head:", stack.get_head())
print("Head:", stack.storage.remove_head())
print("New Head:", stack.get_head())
print("Length:", stack.size)
print("Tail:", stack.get_tail())