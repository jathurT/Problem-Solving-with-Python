class Solution(object):
    def isHappy(self, n):
        fast = n
        slow = n
        while True:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(fast)
            fast = digitSquareSum(fast)
            if slow == fast:
                break
        return slow == 1

def digitSquareSum(n):
    sum = 0
    while n:
        sum += (n % 10) * (n % 10)
        n //= 10
    return sum
