class Solution:

    def encode(self, strs: List[str]) -> str:
        len_strs = [len(string) for string in strs]
        encoded_str_list = []
        for i in range(len(strs)):
            encoded_str_list.append(f"{len_strs[i]}#{strs[i]}") 
        return "".join(encoded_str_list)    

    def decode(self, s: str) -> List[str]:
        strs = []
        num_char = ''
        i = 0
        while i < len(s):
            num_char = num_char + s[i]
            if s[i] == '#':
                len_str = int(num_char[:-1])
                num_char = ''
                strs.append(s[i + 1: i + 1 + len_str])
                i = i + 1 + len_str
            else:
                i = i + 1
        return strs




