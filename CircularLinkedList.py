class CircularLinkedListNode:
    # Node class
    def __init__(self, data):
        """
        Initialize the Node class
        """
        self.data = data
        self.next = None

class CircularLinkedList:
    # Linked List class
    def __init__(self):
        """
        Initialize the Circular Linked List
        """
        self.last = None
        self.number_nodes = 0

    def insert_at_beginning(self, new_data):
        """
        Function to insert a value at the beginning
        """
        new_node = CircularLinkedListNode(new_data)
        
        if not self.last:
            self.last = new_node
            self.last.next = self.last
            self.number_nodes += 1
            return

        new_node.next = self.last.next
        self.last.next = new_node
        self.number_nodes += 1

    
    def insert_at_end(self, new_data):
        """
        Function to insert a value at the end
        """
        new_node = CircularLinkedListNode(new_data)

        if self.last == None:
            self.last = new_node
            self.last.next = self.last
            self.number_nodes += 1
            return

        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
        self.number_nodes += 1

    def insert_at_index(self, position, new_data):
        """
        Function to insert a value in the provided index
        """
        new_node = CircularLinkedListNode(new_data)

        if not self.last:
            self.last = new_node
            self.last.next = self.last
            self.number_nodes += 1
            return

        x = 0
        current = self.last
        prev = None
        while x != position:
            prev = current
            current = current.next
            x += 1

        prev.next = new_node
        new_node.next = current
        self.number_nodes += 1

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
        current = self.last.next
        while x != position:
            current = current.next
            x += 1
        current.data = new_data
        return current.data

    def delete_node(self, position: int):
        """
        Function that delete a node according to the provided index
        """
        prev = self.last
        x = 0
        current = self.last.next
        while x != position:
            prev = current
            current = current.next
            x += 1
        prev.next = current.next
        current = None
        self.number_nodes -= 1

    def contains(self, data):
        """
        Function that returns a boolean that indicates 
        if the value provided is in the Linked List
        """
        current = self.last.next
 
        for _ in range(self.number_nodes):
            if current.data == data:
                return True
            current = current.next
 
        return False

    def lenght(self) -> int:
        """
        Function that returns the length of the Linked List
        """
        return self.number_nodes

    def reverse_list(self):
        """
        Function that return the reversed form of the Linked List
        """
        prev = None
        current = self.last.next
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.last = prev

    def sort_list(self):
        """
        Function to sort the Linked List(Bubble Sort). The result is an Ascendent Sort
        """
        if not self.last:
            return
        temp = self.last.next
        for _ in range(self.number_nodes):
            i=temp.next
            for _ in range(self.number_nodes):
                if temp.data < i.data:
                    n=i.data
                    i.data=temp.data
                    temp.data=n
                i=i.next
            temp=temp.next

    def print_list(self):
        """
        Function to print the Linked List
        """
        temp = self.last.next
        for _ in range(self.number_nodes):
            print (f"{temp.data} \n  ↓ ")
            temp = temp.next
        print(f' ⟳ \n{temp.data}')
