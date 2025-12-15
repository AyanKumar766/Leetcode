class Solution:
    def getDescentPeriods(self, prices):
        a = len(prices)
        number = a
        def check(prices):
          local_number = 0
          for i in range(len(prices)-1):
            if prices[i]-prices[i+1]==1:
              local_number += 1
            else:
              break
          return local_number
        
        if not prices:
            return 0

        count = 0
        current_streak = 0

        for i in range(len(prices)):
            if i == 0 or prices[i-1] - prices[i] != 1:
                current_streak = 1
            else:
                current_streak += 1
            
            count += current_streak

        return count
