from utils.io import read_input
from typing import Optional
class Node:
    def __init__(self, key=0, val=0) -> None:
        self.next: Optional[Node] = None
        self.prev: Optional[Node]= None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity = 1) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        self._remove(self.cache[key])
        node = Node(key, key)
        self._insert_front(node)
        self.cache[key] = node
        return self.cache[key]
    
    def put(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, key)
        self._insert_front(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            assert lru is not None
            self._remove(lru)
            del self.cache[lru.key]
        
    def _remove(self, node: Node):
        assert node.prev is not None
        assert node.next is not None
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        assert self.head.next is not None, "head.next should never be None, invariant violated"
        assert self.head.next.prev is not None
        self.head.next.prev = node
        self.head.next = node

        
def simulate_lru(k, requests):
    misses = 0
    lruCache = LRUCache(k)
    for req in requests:
        if lruCache.get(req) != -1:
            continue
        else:
            lruCache.put(req)
            misses += 1
    return misses



if __name__ == "__main__":
    k, requests = read_input("example.in")
    misses = simulate_lru(k, requests)
    print(misses)

# 2 6
# 1 2 1 3 1 2
# cache  = 1 3
# misses = 4