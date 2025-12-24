class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        current_capacity = 0

        for i, cap in enumerate(capacity):
            current_capacity += cap
            if current_capacity >= total_apples:
                return i + 1
        return -1