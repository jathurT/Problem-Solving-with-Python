class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 0:
            x = int(str(x)[1:][::-1]) * -1
        else:
            x = int(str(x)[::-1])
        # 2 ** 31 = 2147483648 and 2 ** 31 - 1 = 2147483647
        if x < (-2 ** 31) or x > (2 ** 31 - 1):
            return 0
        return x
