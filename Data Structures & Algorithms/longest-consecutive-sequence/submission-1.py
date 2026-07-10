class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start_num_set = set()
        start_num_dict = {}
        maxlen = 0
        for num in nums:
            
            if not (num - 1) in num_set:
                start_element = num
                start_num_set.add(start_element)
                count = 1
                seq_list = [start_element]
                while True:
                    if num + count in num_set:
                        seq_list.append(num + count)
                        count = count + 1
                    else:
                        break
                seq_len = len(seq_list)
                if seq_len > maxlen:
                    maxlen = seq_len
                    max_seq = seq_list
        return maxlen


            