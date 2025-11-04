class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []     
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = {}
            for num in window:
                freq[num] = freq.get(num, 0) + 1
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            total = 0
            for idx, (val, count) in enumerate(sorted_items):
                if idx == x:
                    break
                total += val * count
            
            ans.append(total)
        
        return ans
