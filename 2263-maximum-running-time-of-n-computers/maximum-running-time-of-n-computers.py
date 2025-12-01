class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        summ = sum(batteries)
        batteries.sort()
        while batteries[-1] > summ//n:
            summ -= batteries.pop()
            n -= 1
        return summ//n