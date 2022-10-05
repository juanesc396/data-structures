class LinkedListNode:
    # Node class
    def __init__(self, node_data):
        """
        Initialize the Node class
        """
        self.data = node_data
        self.next = None

class LinkedList:
    # Linked List class
    def __init__(self):
        """
        Initialize the Linked List
        """
        self.head = None

    def insert_at_beginning(self, new_data):
        """
        Function to insert a value at the beginning
        """
        new_node = LinkedListNode(new_data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, new_data):
        """
        Function to insert a value at the end
        """
        new_node = LinkedListNode(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
    
        last.next = new_node

    def insert_at_index(self, position, new_data):
        """
        Function to insert a value in the provided index
        """
        new_node = LinkedListNode(new_data)

        if self.head == None:
            self.head = new_node
            return

        x = 0
        current = self.head
        prev = None
        while x != position:
            prev = current
            current = current.next
            x += 1

        prev.next = new_node
        new_node.next = current

    def get_node(self, position: int):
        """
        Function to get the value of the node by index
        """
        x = 0
        current = self.head
        while x != position:
            current = current.next
            x += 1
        return current.data

    def edit_node(self, position: int, new_data):
        """
        Function that allow to edit the value of the node according to the index
        """
        x = 0
        current = self.head
        while x != position:
            current = current.next
            x += 1
        current.data = new_data
        return current.data

    def delete_node(self, position: int):
        """
        Function that delete a node accodring to the provided index
        """
        if position == 0:
            self.head = self.head.next
            return
        x = 1
        current = self.head
        while x <= position:
            prev = current
            current = current.next
            x += 1
        prev.next = current.next
        current = None

    def contains(self, data):
        """
        Function that returns a boolean that indicates 
        if the value provided is in the Linked List
        """
        current = self.head
 
        while current:
            if current.data == data:
                return True
 
            current = current.next
 
        return False

    def length(self) -> int:
        """
        Function that returns the length of the Linked List
        """
        if not self.head:
            return None
        x = 1
        current = self.head
        while current.next:
            current = current.next
            x += 1

        return x

    def reverse_list(self):
        """
        Function that return the reversed form of the Linked List
        """
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def compare_with(self, list2) -> bool:
        """
        Function that compare two list and return if those are equals or not
        """
        value_1 = self.head
        value_2 = list2.head
    
        while 1:
            if value_1 == None or value_2 == None:
                return value_1 == value_2
            elif value_1.data != value_2.data:
                return False
            elif value_1.data == value_2.data:
                value_1 = value_1.next
                value_2 = value_2.next

    def sort_list(self):
        """
        Function to sort the Linked List. The result is an Ascendent Sort
        """
        if not self.head:
            return
        temp = self.head
        while temp:
            i=temp.next
            while i:
                if temp.data > i.data:
                    n=i.data
                    i.data=temp.data
                    temp.data=n
                i=i.next
            temp=temp.next

    def print_list(self):
        """
        Function to print the Linked List
        """
        temp = self.head
        while temp:
            print (f"{temp.data} \n |\n v"),
            temp = temp.next

    