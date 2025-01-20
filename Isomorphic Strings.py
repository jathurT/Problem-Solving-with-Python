class Solution(object):

    # Approach 1
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     return self.isIsomorphicHelper(s, t) and self.isIsomorphicHelper(t, s)
    #
    # def isIsomorphicHelper(self, s, t):
    #     dict = {}
    #     for i in range(len(s)):
    #         if s[i] not in dict:
    #             dict[s[i]] = t[i]
    #         elif dict[s[i]] != t[i]:
    #             return False
    #     return True

    # Approach 2
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        listA = [0] * 256
        listB = [0] * 256
        for i in range(len(s)):
            charA = s[i]
            charB = t[i]
            if listA[ord(charA)] != listB[ord(charB)]:
                return False
            listA[ord(charA)] = i + 1
            listB[ord(charB)] = i + 1
        return True
