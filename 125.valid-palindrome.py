#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new filtered string.
        filterStr = ""

        # Iterate each character in the string.
        for char in s:
            # If char is alphanumerical, add it to filterStr, and convert to lowercase.
            if char.isalnum():
                filterStr += char.lower()
            # Check if reversed string is equal to filterStr.
            return filterStr == filterStr[::-1]

# @lc code=end
