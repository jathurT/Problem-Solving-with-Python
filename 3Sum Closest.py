from typing import List

class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum = float('inf')
    min_diff = float('inf')

    for i in range(len(nums)-2):
      left, right = i + 1, len(nums) - 1
      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]
        diff = abs(current_sum - target)

        if diff < min_diff:
          min_diff = diff
          closest_sum = current_sum

        if current_sum < target:
          left += 1
        elif current_sum > target:
          right -= 1
        else:
          return current_sum
    return closest_sum


def main():
  solution = Solution()
  nums = [-1, 2, 1, -4]
  target = 1
  result = solution.threeSumClosest(nums, target)
  print(f"The sum closest to {target} is: {result}")

if __name__ == "__main__":
  main()

