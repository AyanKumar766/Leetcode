class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pool = defaultdict(list)

        for pattern in allowed:
            base = pattern[:2]
            top = pattern[2]
            pool[base].append(top)

        @cache
        def dfs(level: str) -> bool:
            if len(level) == 1:
                return True

            next_levels = (
                pool[x + y]
                for x, y in pairwise(level)
            )

            return any(
                dfs(next_level)
                for next_level in product(*next_levels)
            )

        return dfs(bottom)