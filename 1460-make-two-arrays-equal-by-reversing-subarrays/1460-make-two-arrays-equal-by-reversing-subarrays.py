class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for i in target:
            dic1[i] += 1
        for i in arr:
            dic2[i] += 1
        
        if dic1 == dic2:
            return True
        