class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = len(digits)-1
        num = 0
        final = []
        for i in digits:
            num += i * 10**count
            count -=1
        num+=1
        for i in str(num):
            final.append(int(i))
        return final
