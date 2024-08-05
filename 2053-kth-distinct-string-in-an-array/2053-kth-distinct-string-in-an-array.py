class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        thingy = []
        frequency = defaultdict(int)
        for i in arr:
            frequency[i] += 1
        for i in frequency:
            if frequency[i] == 1:
                thingy.append(i)
        if len(thingy) > k-1:
            return thingy[k-1]
        else:
            return ""