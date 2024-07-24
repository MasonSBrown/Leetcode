class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # List to hold tuples of the mapped value and its original index
        mapped_with_index = []
      
        # Iterate over the input numbers' list
        for index, num in enumerate(nums):
            # If the number is 0, get the mapped value for 0, else start with 0
            mapped_num = mapping[0] if num == 0 else 0
            power_of_ten = 1  # To keep track of the decimal place
          
            # Decompose the number into digits and map using the provided mapping
            while num:
                num, digit = divmod(num, 10)
                # Map the digit, adjust decimal place and add to the mapped number
                mapped_num = mapping[digit] * power_of_ten + mapped_num
                power_of_ten *= 10  # Increase the decimal place
          
            # Append the tuple of mapped number and original index to the list
            mapped_with_index.append((mapped_num, index))
      
        # Sort the list according to the mapped numbers, stable for identical values
        mapped_with_index.sort()
      
        # Reconstruct the sorted list using the original indices
        return [nums[i] for _, i in mapped_with_index]
        # def conversion(number):
        #     counter = len(str(number)) - 1
        #     temp = 0
        #     for num in str(number):
        #         num = int(num)
        #         temp += mapping[num] * (10**counter)
        #         counter -=1
        #     return temp
        # x = []
        # s = []
        # h = {}
        # z = {}
        # for index, value in enumerate(nums):
        #     x.append(conversion(value))
        #     s.append(index)
        # for i, value in enumerate(nums):
        #     h[value] = i
        # for i, value in enumerate(x):
        #     z[i] = value
        # x = sorted(x[::-1])
        # #find index order back from h, which contains original x
        # final = []
        # counter = 0
        # for i in h.keys():
        #     if i != x[counter]:
        #         counter+=1
        #         final.append(h[i])
        #     else:
        #         final.append(h[i])
        #         counter = 0
        # print(final)
        # final = []
        # count = 0
        # print(x)
        # # for i in x:
        
            





        