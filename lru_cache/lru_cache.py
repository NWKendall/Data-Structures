from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # limit/max of lru
        self.limit = limit
        # current size
        self.size = 0
        # DLL for order of data
        self.order = DoublyLinkedList()
        # Provides fast access to evert value in order
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
    # check if key exists
        if key not in self.storage:
            return None
    # if key is in cahce
        else:
        # move it to most recently used
            new_tail = self.storage[key]
            self.order.move_to_end(new_tail)
            return new_tail.value[1]
        # return value


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # simplest scenario goes at the bottom as else

        # if item/key already exists
        if key in self.storage:
            # where is the value stored = storage
            node = self.storage[key] # setting node variable to data in storage, referenced by key
            # overwrite the value with the new value
            # overwrites key but same value
            node.value = (key, value)
            # move to the tail (most recently used)
            self.order.move_to_end(node)
            return

        # check to see if size is at limit
        if len(self.order) == self.limit:
            # evict oldest
            # to be Garbage Collected (GC), data must have no pointers
            # as the value of head is a tuple, calling value[0] refers to the key within the tuple
            index_of_oldest = self.order.head.value[0]
            del self.storage[index_of_oldest]
            self.order.remove_from_head()

        # otherwise if size not at limit
        # add to order
        self.order.add_to_tail((key, value))
        # add to storage
        self.storage[key] = self.order.tail
