class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map:
                if map[diff] > i:
                    return [i, map[diff]]
                return[map[diff], i]
            map[n] = i
                
        