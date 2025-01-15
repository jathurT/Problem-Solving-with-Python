class Solution(object):
    def containsDuplicate(self, nums):
        set_nums = set(nums)
        return len(set_nums) != len(nums)