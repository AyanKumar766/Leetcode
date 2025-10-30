class Solution:
    def maxFreqSum(self, s: str) -> int:
        # list of vowels
        vowels = set("aeiou")
        
        # count frequencies of all letters (naive way)
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        # find the maximum frequency among vowels
        max_vowel = 0
        for ch in freq:
            if ch in vowels:
                if freq[ch] > max_vowel:
                    max_vowel = freq[ch]
        
        # find the maximum frequency among consonants
        max_consonant = 0
        for ch in freq:
            if ch not in vowels:
                if freq[ch] > max_consonant:
                    max_consonant = freq[ch]
        
        # return sum
        return max_vowel + max_consonant
