class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket sort
        dict_count = {}
        list_count = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            dict_count[num] = dict_count.get(num, 0) + 1
        
        for key, value in dict_count.items():
            list_count[value].append(key)
        
        for i in range(len(list_count) - 1, 0, -1):
            for n in list_count[i]:
                res.append(n)
            if len(res) == k:
                return res