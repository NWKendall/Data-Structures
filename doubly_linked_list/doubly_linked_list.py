"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # creating node
        new_node = ListNode(value)
        # add value reflecting # of items in LL
        self.length += 1
        # link node to head if list is empty. Becomes both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # list is populated
        else:
        # update the locations of head and tail
            # current head is being linked to new_head
            new_node.next = self.head
            # updating old head to have a prev link
            self.head.prev = new_node
            # updating new head to new-node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # store value before we delete the node, so it can be returned
        value = self.head.value
        # delete head
        self.delete(self.head)
        # return value of deleted node
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        # add value reflecting # of items in LL
        self.length += 1
        # link node to head if list is empty. Becomes both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # list is populated
        else:
        # update the locations of head and tail
        # opposite of add_new_head
            # the prev-prop of new node will be linking to previous tail
            new_node.prev = self.tail
            # current tail's next-prop will link to new node being added
            self.tail.next = new_node
            # updating new tail to new-node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # opposite of remove from head
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # self refers to list
        # node is value passed in as arg
        # -----
        # don't perform if node already is head
        if node is self.head:
            return
        # store node value so is safe to delete and available for adding to head
        value = node.value
        # delete node from current location
        self.delete(node)
        # add to head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # opposite of move_to_front        
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list

        # assuming node is in list
        # reduce # of items in DLL
        self.length -= 1
        # if head & tail, ass
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if head
        elif node is self.head:
            # next node after head becomes new head
            self.head = self.head.next
            node.delete()

        # if tail
        # opposite of head
        elif node is self.tail:       
            self.tail = self.tail.prev
            node.delete()

        # if regular node, call existing delete function
        else:
            node.delete()
    """Returns the highest value currently in the list"""
    def get_max(self):
        # start at head
        if not self.head:
            return None
        # store the head.value in max_val
        max_value = self.head.value
        # create a var for iteration, beginning with first value (head node)
        current = self.head
        # iterate through each node and compare
        # don't use for loop!
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value
            
        # if i > max_val, max_val = i
        # return max_val


