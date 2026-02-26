class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Result array of same length
        result = [0] * n
        
        left, right = 0, n - 1
        # Fill result from end to start
        pos = n - 1

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1

            pos -= 1
        
        return result