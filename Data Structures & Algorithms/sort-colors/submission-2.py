class Solution:
    def sortColors(self, nums: List[int]) -> None:
        k = 0
        pos = 0
        while k <=  2:
            for i in range(len(nums)):
                if nums[i] == k:
                    temp = nums[i]
                    nums[i] = nums[pos]
                    nums[pos] = temp
                    pos += 1
                i += 1
            k += 1