class Solution:
  def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
      return 0

    sign = 1
    index = 0
    if s[0] in ('-', '+'):
      if s[0] == '-':
        sign = -1
      index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
      digit = int(s[index])
      result = result * 10 + digit
      index += 1

    result *= sign
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    return max(INT_MIN, min(result, INT_MAX))
