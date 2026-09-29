class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = None
        k = 0
        for num in nums:
            if num != seen:
                seen = num
                nums[k] = num
                k += 1
        return k
        