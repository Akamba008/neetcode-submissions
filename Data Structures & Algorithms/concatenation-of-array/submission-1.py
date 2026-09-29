class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        length = len(nums)
        while True:
            if count == length:
                count = 0
            ans.append(nums[count])
            count += 1
            if len(ans) == 2*length:
                break
        return ans