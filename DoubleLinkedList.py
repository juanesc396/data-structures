class DoubleLinkedListNode:
    # Node class
    def __init__(self, data):
        """
        Initialize the Node class
        """
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    # Double Linked List class
    def __init__(self):
        """
        Initialize the Double Linked List
        """
        self.head = None

    def insert_at_beginning(self, new_data):
        """
        Function to insert a value at the beginning
        """
        new_node = DoubleLinkedListNode(new_data)

        new_node.next = self.head
        self.head = new_node

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, new_data):
        """
        Function to insert a value at the end
        """
        new_node = DoubleLinkedListNode(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
    
        last.next = new_node

        new_node.prev = last

    def insert_at_index(self, position, new_data):
        """
        Function to insert a value in the provided index
        """
        new_node = DoubleLinkedListNode(new_data)

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
        current.prev = new_node

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
        Function that delete a node according to the provided index
        """
        if position == 0:
            nxt = self.head.next
            nxt.prev = None
            self.head = nxt
            return

        x = 1
        current = self.head
        while x != position:
            prev = current
            current = current.next
            x += 1
        nxt = current.next
        prev.next = nxt
        nxt.prev = prev

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


    def lenght(self) -> int:
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
        current = self.head
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        self.head = prev.prev

    def sort_list(self):
        """
        Function to sort the Linked List with Bubble Sort, swapping the data between nodes. 
        The result is an Ascendent Sort
        """
        if not self.head:
            return

        current = self.head
        while current:            
            compared = current.next
            while compared:
                if current.data > compared.data:
                    temp = current.data
                    current.data = compared.data
                    compared.data = temp
                compared = compared.next
            current = current.next

    def print_list(self):
        """
        Function to print the Double Linked List
        """
        temp = self.head
        while temp:
            print (f"{temp.data} \n ^ \n |\n v")
            temp = temp.next
