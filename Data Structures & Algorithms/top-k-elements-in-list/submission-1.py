class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        output = []
        count = 0
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        for i in range(k):
            max_val = 0
            for key, value in num_freq.items():
                if value > max_val:
                    max_val = value
                    max_key = key
            output.append(max_key)

            if max_key in num_freq:
                num_freq[max_key] = -1
                
        return output