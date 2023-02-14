class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.data = data
            node.next = self.head
        self.head = node
        
    
    def pop_front(self):
        if self.head == None:
            return None
        self.head = self.head.next
    
    def push_back(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


    def pop_back(self):
            if self.head == None:
                return None
            if self.head.next == None:
                pop = self.head.data
                self.head = None
                self.tail = None
                return pop
            else:
                node = self.head
                while node.next.next != None:
                    node = node.next
                pop = node.next.data
                node.next = None
                self.tail = node
                return pop
        

    def get_size(self):
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count


    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data)
            node = node.next
            if node != None:
                ret_str += "\n"
        return ret_str






# lis = LinkedList()
# lis.push_back(3)
# lis.push_back(1)
# lis.push_back(6)
# lis.push_back(9)
# print("container of size: " + str(lis.get_size()) + ":")
# # print("\n")
# print(lis)
# print(lis.pop_front())
# print(lis.pop_front())
# print("container of size: " + str(lis.get_size()) + ":")
# lis = LinkedList()
# lis.push_back(3)
# lis.push_back(1)
# lis.push_back(6)
# lis.push_back(9)
# print(lis)
# new_node = LinkedList()
# for i in range(1, 6):
#     new_node.push_front("string " + str(i))
# print(new_node)
# new_node.pop_back()
# print(new_node)
# new_node.pop_front()
# print("\n")
# print(new_node)
# print(new_node.get_size())
# new_node.append_node(6)
# print(new_node)