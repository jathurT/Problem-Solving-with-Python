class Solution(object):
    # Naive approach O(n^3) time complexity
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     longest = 0
    #     length = len(s)
    #     for i in range(0, length):
    #         seen = set()
    #         for j in range(i, length):
    #             if s[j] in seen:
    #                 break
    #             else:
    #                 seen.add(s[j])
    #         longest = max(longest, len(seen))
    #     return longest

    # Optimized sliding window approach 1
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     longest = 0
    #     length = len(s)
    #     right = 0
    #     left = 0
    #     seen = set()
    #     while right < length:
    #         while s[right] in seen:
    #             seen.remove(s[left])
    #             left += 1
    #         seen.add(s[right])
    #         longest = max(longest, right - left + 1)
    #         right += 1
    #     return longest

    # Optimized sliding window approach 1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        array = [0] * 256
        longest = 0
        left = 0
        for right in range(length):
            left = max(left, array[ord(s[right])])
            longest = max(longest, right - left + 1)
            array[ord(s[right])] = right + 1
        return longest