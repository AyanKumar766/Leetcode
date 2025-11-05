
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)

        TOP, REST, NONE = 1, 0, -1
        where = defaultdict(lambda: NONE)

        # top: min-heap by (freq, value)  -> worst of the top at root
        top = []
        # rest: max-heap by (-freq, -value) -> best of the rest at root
        rest = []

        top_size = 0          # number of distinct values currently in top
        top_sum = 0           # sum over value*freq for keys in top
        distinct = 0

        def push_top(val):
            heapq.heappush(top, (cnt[val], val))

        def push_rest(val):
            heapq.heappush(rest, (-cnt[val], -val))

        def clean_top():
            # pop until heap root reflects current state and membership
            while top:
                f, v = top[0]
                if where[v] != TOP or cnt[v] != f:
                    heapq.heappop(top)
                else:
                    break

        def clean_rest():
            while rest:
                nf, nv = rest[0]
                f, v = -nf, -nv
                if where[v] != REST or cnt[v] != f:
                    heapq.heappop(rest)
                else:
                    break

        def need_top():
            return min(x, distinct)

        def promote():
            nonlocal top_size, top_sum
            clean_rest()
            if not rest:
                return False
            nf, nv = heapq.heappop(rest)
            f, v = -nf, -nv
            # may be stale, but clean_rest guarantees valid
            where[v] = TOP
            top_size += 1
            top_sum += v * cnt[v]
            push_top(v)
            return True

        def demote():
            nonlocal top_size, top_sum
            clean_top()
            if not top:
                return False
            f, v = heapq.heappop(top)
            # valid because clean_top ensures it
            where[v] = REST
            top_size -= 1
            top_sum -= v * cnt[v]
            push_rest(v)
            return True

        def rebalance():
            # 1) size fix
            while top_size < need_top():
                if not promote():
                    break
            while top_size > need_top():
                if not demote():
                    break
            # 2) ordering fix: best(rest) should not beat worst(top)
            while True:
                clean_top(); clean_rest()
                if not top or not rest:
                    break
                f_top, v_top = top[0]
                f_rest, v_rest = -rest[0][0], -rest[0][1]
                if (f_rest > f_top) or (f_rest == f_top and v_rest > v_top):
                    # swap them
                    demote()   # kicks current worst top to rest
                    promote()  # pulls current best rest to top
                else:
                    break

        def add(val):
            nonlocal distinct, top_sum, top_size
            old = cnt[val]
            if old == 0:
                distinct += 1
                cnt[val] = 1
                # new key starts in REST, may get promoted by rebalance
                where[val] = REST
                push_rest(val)
            else:
                cnt[val] = old + 1
                # push updated state to the right heap
                if where[val] == TOP:
                    top_sum += val  # added one occurrence inside top
                    push_top(val)
                elif where[val] == REST:
                    push_rest(val)
                else:
                    # shouldn't happen
                    where[val] = REST
                    push_rest(val)

            rebalance()

        def remove(val):
            nonlocal distinct, top_sum, top_size
            old = cnt[val]
            # assume old > 0
            cnt[val] = old - 1
            if where[val] == TOP:
                top_sum -= val  # removed one occurrence from top
                push_top(val)   # new (smaller) freq
            elif where[val] == REST:
                push_rest(val)

            if cnt[val] == 0:
                distinct -= 1
                if where[val] == TOP:
                    # it leaves top as a distinct key
                    where[val] = NONE
                    top_size -= 1
                else:
                    where[val] = NONE
                del cnt[val]

            rebalance()

        # build first window
        for i in range(k):
            add(nums[i])

        ans = [top_sum]

        # slide
        for i in range(k, n):
            add(nums[i])
            remove(nums[i - k])
            ans.append(top_sum)

        return ans
