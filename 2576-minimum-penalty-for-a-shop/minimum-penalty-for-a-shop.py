class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0]
        _sum = 0
        i = 0
        while(i < len(customers)):

            if(customers[i] == "N"):
                _sum += 1
            
            prefix.append(_sum)

            i += 1
        
        suffix = [0]
        _sum = 0
        i = len(customers) - 1
        while(i >= 0):
            
            if(customers[i] == "Y"):
                _sum += 1
            
            suffix.append(_sum)
            
            i -= 1
        
        suffix.reverse()

        _min = int(2 ** 31) - 1
        ans = -1
        i = 0 
        while(i < len(prefix)):

            _sum = prefix[i] + suffix[i]
            if(_sum < _min):
                _min = _sum
                ans = i
            i += 1

        return ans