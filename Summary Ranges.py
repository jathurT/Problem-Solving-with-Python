class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                if start == nums[i - 1]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))
        return ranges


if __name__ == "__main__":
    print(Solution().summaryRanges([0, 2, 5, 9]))
