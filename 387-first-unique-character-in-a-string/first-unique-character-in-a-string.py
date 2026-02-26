class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count frequencies of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # find first unique
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        
        return -1