class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        l = 0
        max_len = 0
        for r, ch in enumerate(s):
            char_dict[ch] = char_dict.get(ch, 0) + 1
            while r - l + 1 - max(char_dict.values()) > k:
                char_dict[s[l]] -= 1
                l = l + 1
            max_len = max(max_len, r - l + 1)
        return max_len


        

