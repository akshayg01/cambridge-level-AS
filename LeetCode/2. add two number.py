# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = ListNode(value)
        
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_first(self):
        if not self.head:
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.value

    def delete_last(self):
        if not self.head:
            return None
        if not self.head.next:
            deleted_node = self.head
            self.head = None
            return deleted_node.value
        second_last = self.head
        while second_last.next and second_last.next.next:
            second_last = second_last.next
        deleted_node = second_last.next
        second_last.next = None
        return deleted_node.value




class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        r = LinkedList()
        carryForward = 0
        while(l1 or l2 or carryForward):
            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0
            x = a + b + carryForward
            if (x > 9):
                carryForward = 1
                x = x - 10
            else:
                carryForward = 0
            r.insert_at_end(x)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return r.head
# Example usage:
# Creating first number: 342 (represented as 2 -> 4 -> 3)   
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)  

# Creating second number: 465 (represented as 5 -> 6 -> 4)
l2 = ListNode(5)    
l2.next = ListNode(6)
l2.next.next = ListNode(4)  
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
# Output the result
while result:
    print(result.val, end=" -> ")
    result = result.next


        
        