class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(i < k for i in nums)