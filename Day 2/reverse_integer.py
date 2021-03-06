# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        answer = ''
        isNegative = False
        for i in list(str(x)):
            if i[0] == '-':
                isNegative = True
                continue
            answer = i + answer
        if isNegative:
            answer = -int(answer)
        else:
            answer = int(answer)
        if (answer < -(2**31)) or (answer > (2 ** 31) - 1):
            return 0
        return int(answer)