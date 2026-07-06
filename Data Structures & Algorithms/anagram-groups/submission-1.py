class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            value = dict_str.get(sorted_str, [])
            value.append(s)
            dict_str[sorted_str] = value
        final_list = []
        for key, value in dict_str.items():
            final_list.append(value)
        return final_list
