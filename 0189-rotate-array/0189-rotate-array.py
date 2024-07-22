class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lng = len(nums)
        if k > lng:
            k %= lng

        if k == 0 or lng <= 1:
            return nums

        # tmp = [0] * lng

        # [0 for _ in range(len(nums))]

        # for i in range(len(nums)):
        #     if i + k >= len(nums):
        #         empty_list[(k-len(nums)+i)] = nums[i]
        #     else:
        #         empty_list[(i+k)] = nums[i]
        # nums[:] = empty_list
        
        tmp = nums[lng-k:] + nums[:lng-k]
        nums[:] = tmp



