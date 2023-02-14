class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    if head == None:
        return 0
    else:
        return 1 + get_size(head.next)

def reverse_list(head):
    if head == None or head.next == None :
        return head
    else:
        rev_lis = reverse_list(head.next)
        head.next.next = head
        head.next = None
        return rev_lis



def palindrome(head):
    if head == None:
        return False
    rev_lis = reverse_list(head)
    while head != None:
        if head.data != rev_lis.data:
            return False
        head = head.next
        rev_lis = rev_lis.next
        rev_lis + palindrome(head)
    return True



if __name__ == "__main__":
    ##
    # print("GET_SIZE TESTS")
    # print("\n")
    # head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    # print_to_screen(head)
    # print("size: " + str(get_size(head)))
    # print_to_screen(head)

    # print("\n")
    # head = None
    # print_to_screen(head)
    # print("size: " + str(get_size(head)))
    # print_to_screen(head)

    # print("\n")
    # head = Node("A", None)
    # print_to_screen(head)
    # print("size: " + str(get_size(head)))
    # print_to_screen(head)

    # print("\n")
    # head = Node("A", Node("C", None))
    # print_to_screen(head)
    # print("size: " + str(get_size(head)))
    # print_to_screen(head)


    # ##
    # print("REVERSE TESTS")
    # print("\n")
    # head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)

    # print("\n")
    # head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)

    # print("\n")
    # head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)

    # print("\n")
    # head = Node("C", None)
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)

    # print("\n")
    # head = None
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)

    # print("\n")
    # head = Node("C", Node("B", None))
    # print_to_screen(head)
    # rev_head = reverse_list(head)
    # print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
