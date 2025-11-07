class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]

        def can(x):
            added = [0] * n
            extra = 0
            remain = k
            for i in range(n):
                if i - r - 1 >= 0:
                    extra -= added[i - r - 1]
                window_sum = prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] + extra
                if window_sum < x:
                    need = x - window_sum
                    if need > remain:
                        return False
                    added[min(n - 1, i + r)] = need
                    extra += need
                    remain -= need
            return True

        low, high = 0, prefix[-1] + k
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        return low
