# Using Map to solve this problem
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        for char in t:
            if char not in map:
                return False
            map[char] -= 1
            if map[char] == 0:
                del map[char]
        return not map


# Using sorting to solve this problem
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)