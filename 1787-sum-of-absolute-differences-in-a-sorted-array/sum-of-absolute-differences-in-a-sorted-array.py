class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        result = [0] * n
        
        total_sum = sum(nums)
        prefix_sum = 0
        
        for i in range(n):
            left = nums[i] * i - prefix_sum
            right = (total_sum - prefix_sum - nums[i]) - nums[i] * (n - i - 1)
            
            result[i] = left + right
            prefix_sum += nums[i]
        
        return result