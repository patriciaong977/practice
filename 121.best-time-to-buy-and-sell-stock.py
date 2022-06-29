#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    # Create l and r pointers, and max profit
    ptrL = 0  # Buy in the first day
    ptrR = 1  # Sell in the second day
    maxProfit = 0

    # Keep iterating through the prices while ptrR is < the length of prices.
    while ptrR < len(prices):
      # Check if you made a profit.
      if prices[ptrL] < prices[ptrR]:
        profit = prices[ptrR] - prices[ptrL]
        # Add to max profit if you made a profit.
        # Whatever is the highest will be assigned.
        maxProfit = max(maxProfit, profit)
      else:  # This is if you didn't make a profit.
        ptrL = ptrR  # We want our l to be at the minimum lowest price.
      ptrR += 1  # Whatever the result, update the right pointer.

    return maxProfit

# @lc code=end
