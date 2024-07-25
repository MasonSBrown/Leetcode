class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums[::-1])
        return nums