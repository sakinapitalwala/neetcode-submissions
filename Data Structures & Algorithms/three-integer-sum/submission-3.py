class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:

                if (nums[i] + nums[l] + nums[r]) > 0:
                    r = r - 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l = l + 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l = l + 1
                    r = r - 1
                    while l < r and  nums[l] == nums[l - 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r + 1]:
                        r = r -1
                    
        
        return output
