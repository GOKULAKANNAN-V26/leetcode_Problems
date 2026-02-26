class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the most recent index of each number
        last_seen = {}
        
        for i, value in enumerate(nums):
            if value in last_seen and i - last_seen[value] <= k:
                return True
            # Update most recent index for value
            last_seen[value] = i
        
        return False