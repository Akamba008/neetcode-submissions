class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            if target - n not in map:
                map[n] = map.get(n, i)
            else:
                if map[target - n] < i:
                    index = [map[target - n], i]
                    return index
                index = [i, map[target - n]]
                return index
        