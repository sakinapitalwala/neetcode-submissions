class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        max_len = 0
        for r, ch in enumerate(s):
            if ch in seen  and seen[ch] >= l:
                l = seen[ch] + 1
            seen[ch] = r
            max_len = max(max_len, r - l + 1)

        return max_len    
