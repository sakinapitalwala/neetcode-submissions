class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod2 = 1
        output = []
        count = 0
        for num in nums:
            if num == 0:
                count = count + 1
            prod = prod * num
        if count == 1:
            for num in nums:
                if num != 0:
                    prod2 = prod2 * num
        for num in nums:
            if num == 0 and count == 1:
                output.append(prod2)
            elif num == 0 and count > 1:
                output.append(0)
            else:
                output.append(int(prod/num))
        return output