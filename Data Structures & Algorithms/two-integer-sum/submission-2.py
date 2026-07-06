class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = []
        for i,  num in enumerate(nums):
            num_list.append([num, i])
        num_list.sort()
        i = 0
        j = len(num_list) - 1
        while i < j:
            if num_list[i][0] + num_list[j][0] < target:
                i = i + 1
            elif num_list[i][0] + num_list[j][0] > target:
                j = j - 1
            else:
                return [min(num_list[i][1], num_list[j][1]), max(num_list[i][1], num_list[j][1])]
        