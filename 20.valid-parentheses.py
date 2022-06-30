#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
  def isValid(self, s: str) -> bool:
    # Using a stack to keep track of the parentheses.
    stack = []

    # Create a Hashmap to map the parentheses to their corresponding closing.
    # This will be used to check if the closing parentheses match the opening ones.
    # Closed parenthesis (key) : Open parenthesis (value)
    hashMap = {")": "(", "]": "[", "}": "{"}

    # Iterate through the string to build the stack. For each char in the input string.
    for char in s:
        # Check if the char is the key/closing parenthesis in the hashmap.
        # If the char is in hashMap, then its a closing parenthesis because of the key.
        if char in hashMap:
            # Make sure that stack is NOT empty, we can't h ave a closing parenthesis first.
            # AND Make sure that the top of the stack is == to the value in the hashMap. hashMap[char] is the value.
            # stack[-1] is the last value added to the stack
            if stack and stack[-1] == hashMap[char]:
                # If the above matches, pop/remove from the stack.
                stack.pop()
            else:  # If the above doesn't match or the stack is empty, return False.
                return False
        else:  # If the char is not the key/closing parenthesis in the hashmap,
            # then its an opening parenthesis and add the char it to the stack.
            stack.append(char)

    # Once we've iterated through the string, if the stack is empty, then return true.
    return True if not stack else False


# @lc code=end
