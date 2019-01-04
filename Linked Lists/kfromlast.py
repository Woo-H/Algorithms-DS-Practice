# Write a code to remove the kth element from the end of a singly linked list

# Standard Python implementation of Node object
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

        # Iterate through input list to create linked lists
        for item in input_list:
            curr = Node(item)
            tail.next = curr
            tail = curr

        return head.next

    # Method for removing kth from last item
    # Runner starts first. Chaser begins after k iterations. Both end when runner.next = null
    def remove_k(self, k, head):
        r, c = head, head
        c_head = c
        i = 0 
        while 1:
            if r.next == None:
                if i < k:
                    print('k is larger than the lenght of the linked list')
                c.next = c.next.next
                break
            else:
                r = r.next  
                i += 1
            if i > k:
                c = c.next
        return c_head

    def print_elements(self, head):
        while 1:
            print(head.val)
            if head.next == None:
                print('End of Linked List')
                break
            head = head.next

# Testing Solution
test = Solution()
head = test.generate_linked_list([1,4,5,7,3,4,5,1,2,3,4,9,3,4,6,1])

print('Original Linked List: ')
test.print_elements(head)

k = int(input('k = ?: '))
print('Removing {}th element from end'.format(k))
head_new = test.remove_k(k, head)

print('Linked List after Removing kth element from end: ')
test.print_elements(head_new)
