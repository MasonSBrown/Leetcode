class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (len(x) % 2) != 0:
            math = len(x) / 2
            x = x[:int(math)] + x[int(math)+1:]

        for i in range(len(x)):
            if x[i] != x[-i-1]:
                return False
        return True