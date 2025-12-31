class Solution:
    def hammingWeight(self, n: int) -> int:        
        temp = format(n, 'b')
        count = 0
        for i in temp:
            if int(i) == 1:
                count += 1
        return count

