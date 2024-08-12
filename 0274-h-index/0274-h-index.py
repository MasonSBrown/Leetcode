class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        lowestcit = 0
        while lowestcit < length:
            lowestcit = min(citations)
            print(lowestcit)
            if lowestcit >= length:
                return length
            else:
                length-=1
                citations.remove(lowestcit)
        return length
                            