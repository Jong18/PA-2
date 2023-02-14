from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()
        # self.container = ArrayDeque()

    def push(self, data):
        self.container.push_back(data)
    
    def pop(self):
        popped_element = self.container.pop_back()
        return popped_element
    
    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
