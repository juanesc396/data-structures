from platform import node


class HashTableNode:
    # Node class to Hash Table with separate chaining
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f'Key: {self.key} - Value: {self.value} \
        \n ↓ \n{self.next}'

    def to_list(self) -> list:
        """
        Function that return a list of tuples with the key and
        values of the linked list
        """
        l = [(self.key, self.value)]
        nxt = self.next
        while nxt:
            l.append((nxt.key, nxt.value))
            nxt = nxt.next

        return l

class SeparateChainingHashTable:
    # Hash Table class with separate chaining
    def __init__(self, size = 37):
        self.size = size
        self.buckets = [None for _ in range(size)]


    def _hash(self, key):
        """
        Function that return an hash value to then, 
        interact with a node into a Hash Table
        """
        temp = hash(key)
        if temp < 0:
            temp = temp *-1
        temp = round(temp / (10*16))
        index = temp % self.size 
        return index
    
    def insert(self, key, value):
        """
        Function that insert a node into a Hash Table
        """
        index = self._hash(key)
        new_node = HashTableNode(key, value)

        node = self.buckets[index]

        if not node:
            self.buckets[index] = new_node
        else:
            prev = node
            while node:
                prev = node
                node = node.next
            prev.next = new_node

    def find(self, key) -> object:
        """
        Function that helps to find a node into a Hash Table
        """
        index = self._hash(key)
        node = self.buckets[index]

        while node and node.key != key:
            node = node.next
        if node is None:
            raise KeyError('Key Not Found')
        else:
            return node

    def delete(self, key):
        """
        Function that remove a node into a Hash Table
        """
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        while node and node.key != key:
            prev = None
            node = node.next

        if not node:
            return None
        else:
            result = node.value

            if not prev:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
