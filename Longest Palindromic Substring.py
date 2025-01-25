class Solution(object):

    # Brute force approach
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        pal_str = ""
        for i in range(length):
            for j in range(i + 1, length + 1):
                sub = s[i:j]
                if (self.is_palindrome(sub)) and (len(sub) > len(pal_str)):
                    pal_str = sub
        return pal_str

    @staticmethod
    def is_palindrome(sub):
        return sub == sub[::-1]
