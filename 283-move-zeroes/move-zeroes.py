class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # pointer for where the next non-zero element should go
        j = 0

        # First pass: move non-zeros to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Second pass: fill the rest with zeros
        for k in range(j, len(nums)):
            nums[k] = 0