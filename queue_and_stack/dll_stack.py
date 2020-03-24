import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        # because we need to keep track of the front and back of the queue
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.len() < 1:
            return
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
