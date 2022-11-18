from multiprocessing import Value


class HashTableNode:
    # Node class to Hash Table with Open Addressing(Linear Probing)
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f'Key: {self.key} - Value: {self.value}'

class OpenAddressingHashTable:
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
        while node:
            index += 1
            node = self.buckets[index]
        if node:
            raise KeyError
        self.buckets[index] = new_node
    
    def find(self, key) -> list:
        """
        Function that helps to find a node into a Hash Table.
        Return a list of values
        """
        l = []
        index = self._hash(key)
        node = self.buckets[index]
        if node:
            l.append(node.value)
        try:
            while self.buckets[index+1]:
                next_node = self.buckets[index+1]
                l.append(next_node.value)
                index += 1
        except:
            pass
        if len(l)>0:
            return l
        raise KeyError('Key Not Found')

    def delete(self, key):
        """
        Function that remove a node into a Hash Table
        """
        index = self._hash(key)
        node = self.buckets[index]
        
        if not node:
            raise KeyError('Key Not Found')
        elif node.key == key:
                self.buckets[index] = None
