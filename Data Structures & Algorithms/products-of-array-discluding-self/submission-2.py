class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = []
        prod_rev = [1 for i in range(len(nums))]
        prod = 1
        output = []
        for num in nums:
            prod = prod * num
            prod_arr.append(prod)
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod = prod * nums[i]
            prod_rev[i] = prod
        for i in range(len(nums)):
            if i == 0:
                output.append(prod_rev[i+1])
            elif i == len(nums) - 1:
                output.append(prod_arr[i-1])
            else:
                output.append(prod_arr[i-1] * prod_rev[i+1])
        return output