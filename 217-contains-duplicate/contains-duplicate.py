class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp = len(set(nums))
        if temp != len(nums):
            return True
        else:
            return False