class MyHashMap:

    def __init__(self):
        self.set = [[] for _ in range(10)]
        

    def put(self, key: int, value: int) -> None:
        hash = key % len(self.set)
        for pair in self.set[hash]:
            if pair[0] == key:
                pair[1] = value
                return None
        self.set[hash].append([key, value])
        

    def get(self, key: int) -> int:
        hash = key % len(self.set)
        for pair in self.set[hash]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        hash = key % len(self.set)
        for pair in self.set[hash]:
            if pair[0] == key:
                self.set[hash].remove(pair)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)