class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)

        if k == 0 or len(nums) <= 1:
            return nums

        empty_list = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i + k >= len(nums):
                empty_list[(k-len(nums)+i)] = nums[i]
            else:
                empty_list[(i+k)] = nums[i]
        nums[:] = empty_list
