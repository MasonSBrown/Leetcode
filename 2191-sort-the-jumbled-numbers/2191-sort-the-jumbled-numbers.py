class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def conversion(number):
            counter = len(str(number)) - 1
            temp = 0
            for num in str(number):
                num = int(num)
                temp += mapping[num] * (10**counter)
                counter -=1
            return temp
        paired_numbers = []
        for value in nums:
            converted_value = conversion(value)
            paired_numbers.append((converted_value, value))
        paired_numbers.sort(key=lambda x: x[0])
        sorted_nums = [value for _, value in paired_numbers]
        return sorted_nums