class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds_up_to_high = (high + 1) >> 1
        odds_before_low = low >> 1
        return odds_up_to_high - odds_before_low
