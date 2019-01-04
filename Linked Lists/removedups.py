# Write a code to remove deuplicates from an unsorted linked list

# Standard Python implementation of Node object
class Node: 

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: 

    def __init__(self, dummy = 0):
        self.dummy_head = Node(dummy)

    def generate_linked_list(self, input_list):
        head = self.dummy_head	
        tail = head

        # Iterate through input list to create linked lists
        for item in input_list:
            curr = Node(item)
            tail.next = curr
            tail = curr

        return head.next

    # Method for removing duplicates
    def remove_dups(self, target):
        buffer = []

        while target.next != None:
            i = target.val         
            if i not in buffer:  
                buffer.append(i)
                print(buffer)
            target = target.next

        new_node = Solution()
        new_linked_list = new_node.generate_linked_list(buffer)
 
        return new_linked_list
 
    # Method for printing all elements of the linked list
    def print_elements(self, head):
        while 1:
            print(head.val)
            if head.next == None:
                print('Linked list ended')
                break
            head = head.next

# Testing Solution
test = Solution()
head = test.generate_linked_list(input_list = [1,2,3,7,1,9,8,3,1,7])

print('Original Linked List: ')
test.print_elements(head)

head_new = test.remove_dups(head)

print('Linked List after Removing Duplicates: ')
test.print_elements(head_new)
