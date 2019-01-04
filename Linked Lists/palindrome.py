# Write a code to check if a linked list is a palindrome
# Will assume the case of a doulbly linked list

# Standard Python implementation of Node object for doubly linked list
class Node:

    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class Solution:

    def __init__(self, dummy = 0):
        self.dummy_head = Node(dummy)

    # input list accepts strings as well
    def generate_linked_list(self, input_list):
        head = self.dummy_head
        tail = head
        # Iterate through input list to create singly linked lists
        for item in input_list:
            curr = Node(item)
            tail.next = curr
            tail = curr
        # Second iteration to create a doubly linked list
        tail = head.next
        while tail.next != None:
            buffer = tail
            tail = tail.next
            tail.prev = buffer
            buffer = buffer.next
        return head.next

    # Print elements of a doubly linked list. Default is Forward pass.
    def print_elements(self, head, direction = 'forward'):
        if direction == 'forward':
            while 1:
                print(head.val)
                if head.next == None:
                    print('End of Linked List')
                    break
                head = head.next
        elif direction == 'backward':
            while 1:
                print(head.val)
                if head.prev == None:
                    print('End of Linked List')
                    break
                head = head.prev
        else:
            direction = str(input('Re-enter Direction (forward or backward)?: '))
            self.print_elements(head, direction)

    # Recursive Method
    def palindrome(self, head, tail):
        # First condition for odd length, second condition for even length
        if head == tail or head.prev == tail:
            return True
        else:
            # Check element matching and pass on recursively
            if head.val == tail.val:
                print('matched element')
                head = head.next
                tail = tail.prev
                return self.palindrome(head, tail)
            else:
                return False

# Testing Solution
test = Solution()
word = str(input('What string do you want to test?: '))
head = test.generate_linked_list(word)

print('Original Linked List (forward pass): ')
test.print_elements(head, direction = 'forward')

tail_end = head
while tail_end.next != None:
    tail_end = tail_end.next

print('Original Linked List (backward pass): ')
test.print_elements(tail_end, direction = 'backward')

print('Is this a Palindrome?: ', test.palindrome(head, tail_end))
