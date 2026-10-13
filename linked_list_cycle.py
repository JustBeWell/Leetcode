# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
          return False

        slow_pointer = head
        fast_pointer = head

       

        if fast_pointer.next == None:
          return False
        elif slow_pointer == fast_pointer.next:
          return True

        while fast_pointer != None:
          slow_pointer = slow_pointer.next
          fast_pointer = fast_pointer.next

          if fast_pointer == None:
            return False
          
          fast_pointer = fast_pointer.next

          if fast_pointer == None:
            return False

          if slow_pointer == fast_pointer:
            return True


        