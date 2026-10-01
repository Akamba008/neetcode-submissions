class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        count = 0
        while count < length - 1:
            for i in range(length - 1 - count):
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
            count += 1
        return nums