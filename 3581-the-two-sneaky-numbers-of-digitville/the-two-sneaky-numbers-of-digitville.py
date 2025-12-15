class Solution:
    def getSneakyNumbers(self, nums):
        nums.sort()
        temp = []
        for i in nums:
          if nums.count(i) == 2:
            temp.append(i)
        return list(set(temp))
