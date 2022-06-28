#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a Hashmap. Val : Index
        hashMap = {}

        # Iterate every value in the array. Use enumerate to get the index.
        # i is the index, v is the value. i.e. nums[i] = v
        for i, v in enumerate(nums):
            difference = target - v  # Check the diff before adding to map.

            # Check if the difference is in the map.
            if difference in hashMap:  # If it is, return the index.
                # Return the index of the difference.
                return [hashMap[difference], i]

            # If the difference is not in the map, add it to the map.
            hashMap[v] = i

        return []

# @lc code=end
