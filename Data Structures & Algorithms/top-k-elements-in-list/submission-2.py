class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        frequency = []
        for key, value in hashmap.items():
            frequency.append([key, value])  

        k_frequent = []
        maximum = 0
        max_value = None
        for _ in range(k):
            for i in range(len(frequency)):
                if frequency[i][1] > maximum:
                    maximum = frequency[i][1]
                    max_value = frequency[i][0]
            k_frequent.append(max_value)
            frequency.remove([max_value, maximum])
            maximum = 0
        return k_frequent