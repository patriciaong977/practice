#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a Hashset.
        hashSet = set()

        # Check n in nums.
        for n in nums:
            # If n is in hashSet, return true.
            if n in hashSet:
                return True
            # If n is not in the hashset, add to hashset.
            hashSet.add(n)
        return False

# @lc code=end
