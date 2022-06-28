#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create left and right pointers
        l = 0
        r = len(s) - 1  # Length of the string - 1.

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            # Update pointers to move to next comparison
            l = l + 1
            r = r - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    ''' # Solution 1:
    class Solution:
      def isPalindrome(self, s: str) -> bool:
        # Create filtered string
        filterStr = ""
        # Iterate each char in str.
        for char in s:
          # If char is alpha-numeric, add to filtered string, convert to lowercase.
          if char.isalnum():
            filterStr += char.lower()
            # Check reversed string if its equal (Palindrome)
            return filterStr == filterStr[::-1] # Returns true if =, false otherwise.
    '''
# @lc code=end
