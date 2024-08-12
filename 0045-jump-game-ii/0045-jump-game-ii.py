class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # if nums[0] >= len(nums):
        #     return 1
        # index, counter = 0, 0
        # while index < (len(nums) - 1):
        #     for i in range(nums[index]):
        #         if index+i < len(nums)-1:
        #             if nums[index+i] > nums[index]:
        #                     index += i
        #             else:
        #                 index += nums[index]
        #     counter+=1
        # return counter
        #               dont understand question bruh

        ans = 0
        end = 0
        farthest = 0

        #Implicit Breadth First Search

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest
        return ans

        
                