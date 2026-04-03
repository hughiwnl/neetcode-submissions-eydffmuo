class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right = Node(0,0)
        self.left = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        nxt = self.right
        prev = self.right.prev

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
