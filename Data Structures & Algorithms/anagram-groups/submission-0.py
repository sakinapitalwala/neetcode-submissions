class Solution:
    def areAnagrams(self, a, b):
        if len(a) != len(b):
            return False
        dict_a = {}
        dict_b = {}
        for i in a:
            dict_a[i] = dict_a.get(i, 0) + 1
        for i in b:
            dict_b[i] = dict_b.get(i, 0) + 1
        return dict_a == dict_b
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        seen = set()
        for i in range(0, len(strs)):
            if not i in seen:
                l = [strs[i]]
                if i < len(strs) - 1:
                    for j in range(i + 1, len(strs)):                   
                        if not j in seen and self.areAnagrams(strs[i], strs[j]):
                            l.append(strs[j])
                            seen.add(j)
                if l:
                    final_list.append(l)
        return final_list


    


