class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        output = []
        count = 0
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        sorted_dict = dict(sorted(num_freq.items(), key = lambda x: x[1], reverse = True))
        for key, value in sorted_dict.items():
            if count < k:
                output.append(key)
                count = count + 1
        return output