class Solution:
    def findUnion(self, a, b):
        seen = {}  
        union = []

        for num in a + b:  
            if num not in seen:
                seen[num] = True
                union.append(num)

        return union
