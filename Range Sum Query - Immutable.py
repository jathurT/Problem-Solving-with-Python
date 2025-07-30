from typing import List


class NumArray:

  def __init__(self, nums: List[int]):
    self.n = len(nums)
    self.prefix_sum = [0] * (self.n + 1)

    for i in range(self.n):
      self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

  def sumRange(self, left: int, right: int) -> int:
    if self.n == 0:
      return 0
    return self.prefix_sum[right + 1] - self.prefix_sum[left]
