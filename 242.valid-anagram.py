#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # Solution 1: Hash Table
        # If the lengths are not equal, its not an anagram.
        if len(s) != len(t):
            return False

        # Create counter for s and t.
        # Counts each occurence of each letter in s and t.
        countS, countT = {}, {}

        # Count the occurence of each letter in s.
        for i in range(len(s)):
            # Add 1 to the count of the letter if it exists, otherwise add 0.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:  # Iterate through the letters in s
            # If the count of the letter in s is not equal to the count of the letter in t, return False.
            if countS[c] != countT.get(c, 0):
                return False
        # If all letters in s are equal to the letters in t, return True.
        return True

    """ Solution 2: Counter()
    def isAnagram(self, s: str, t: str) -> bool:
      return Counter(s) == Counter(t)
    """

# @lc code=end
