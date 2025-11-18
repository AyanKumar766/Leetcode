class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        length = len(bits)
        while index < length - 1 :
            index += bits[index] + 1
        return index == length - 1