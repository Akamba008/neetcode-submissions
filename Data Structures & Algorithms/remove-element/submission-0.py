class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        if len(nums) == 1:
            if nums[0] != val:
                k += 1
            return k
        for i, num in enumerate(nums):
            if num != val:
                temp = num
                nums[i] = nums[k]
                nums[k] = temp
                k += 1
        return k