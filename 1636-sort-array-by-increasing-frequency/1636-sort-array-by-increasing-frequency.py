class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_frequency = Counter(nums)
        
        sorted_nums = sorted(nums, key=lambda x: (num_frequency[x], -x))
      
        return sorted_nums
        

            

        
            


            