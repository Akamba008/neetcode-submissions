class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = nums[0]
        k = 1
        for num in nums[1:]:
            if num != seen:
                seen = num
                nums[k] = num
                k += 1
        return k
        