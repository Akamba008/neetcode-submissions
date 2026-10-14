class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]

        post = 1
        j = len(nums) - 1
        while j >= 0:
            output[j] *= post
            post *= nums[j]
            j -= 1
        return output