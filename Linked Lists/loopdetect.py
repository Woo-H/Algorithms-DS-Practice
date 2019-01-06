# Write a code to detect the beginning of a loop in a singly linked list

# Standard Python implementation of Node object
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, dummy = 0):
        self.dummy_head = Node(dummy)

    # Loop back from end to the kth node
    def generate_linked_list(self, input_list, k):
        head = self.dummy_head
        tail = head
        c = 0
        # Iterate through input list to create linked lists
        for item in input_list:
            curr = Node(item)
            tail.next = curr
            tail = curr
            if c == k:
                loop_head = curr
            c += 1
        tail.next = loop_head
        return head.next, loop_head

    # Brute force method
    def loop_detect_brutef(self, head):
        memory = []
        print('Running through linked list ...')
        while 1:
            print('Node val: ', head.val)
            memory.append(head)
            head = head.next
            if head in memory:
                print('Loop detected: ', head.val)
                break
        return head


# Testing Solution
test = Solution()
test_list = [1,2,3,7,1,9,8,3,1,7]
k = int(input('which node is loop head?: '))
head, true_loop_head = test.generate_linked_list(input_list = test_list, k = k)

print('Original Linked List: ', test_list)

loop_head = test.loop_detect_brutef(head)

print('Calculated loop head is {} with value {}. This matches answer: {}'.format(loop_head, loop_head.val, loop_head == true_loop_head))
