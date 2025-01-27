# Brute force approach
# Time complexity: O(n^2)
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if (nums[i] == nums[j]) and abs(i - j) <= k:
#                     return True
#         return False

# Optimized approach - using dictionary
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         dict = {}
#         for i in range(len(nums)):
#             if nums[i] in dict and abs(i - dict[nums[i]]) <= k:
#                 return True
#             dict[nums[i]] = i
#         return False

# Sliding window approach
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False


