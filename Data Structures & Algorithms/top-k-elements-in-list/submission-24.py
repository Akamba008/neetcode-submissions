class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        final = []
        frequency_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for value, count in hashmap.items():
            frequency_list[count].append(value)
        
        j = 0
        i = len(frequency_list) - 1
        while i > 0 and j < k:
            if frequency_list[i] != []:
                final.extend(frequency_list[i])
                j += len(frequency_list[i])
            i -= 1
        return final


