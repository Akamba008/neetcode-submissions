class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            combined = []
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    combined.append(a[i])
                    i += 1
                else:
                    combined.append(b[j])
                    j += 1

            while i < len(a):        
                combined.append(a[i])
                i += 1
            while j < len(b):        
                combined.append(b[j])
                j += 1
            return combined

        if len(nums) == 1:
            return nums
        mid = int(len(nums) / 2)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge(left, right)
        