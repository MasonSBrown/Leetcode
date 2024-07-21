class Solution:
    def addBinary(self, a: str, b: str) -> str:
        prebinary = int(a, 2) + int(b, 2)
        answer = bin(prebinary)[2:]
        return answer