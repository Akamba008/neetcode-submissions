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
        for i in range(len(frequency_list) - 1, 0, -1):
            for n in frequency_list[i]:
                final.append(n)
                if len(final) == k:
                    return final

