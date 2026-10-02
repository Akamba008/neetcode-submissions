class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        k_frequent = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        max_count = 0
        max_value = None
        for _ in range(k):
            for value, count in hashmap.items():
                if count > max_count:
                    max_count = count
                    max_value = value
            k_frequent.append(max_value)
            hashmap.pop(max_value)
            max_count = 0
        return k_frequent