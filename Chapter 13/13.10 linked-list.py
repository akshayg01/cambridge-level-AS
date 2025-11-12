class LinkedListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Head or start-pointer should return linked Node ...
# insert-at-beginning
# insert-at-end
# delete-first
# delete-last

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = LinkedListNode(value)
        
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

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


students = LinkedList()
students.insert_at_end("Alice")
students.insert_at_beginning("Bob")
students.insert_at_end("Charlie")
students.display()  # Output: Bob -> Alice -> Charlie -> None   

