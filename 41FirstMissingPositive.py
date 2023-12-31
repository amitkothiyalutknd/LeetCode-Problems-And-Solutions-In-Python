# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        missingNumber, nums = 1, set(nums)
        while missingNumber in nums:
            missingNumber +=1
        return missingNumber

sol = Solution()
nums = list(map(int, input(f"Enter The Numbers For An Array. Seperate Each Input From Single Space: ").strip().split()))[:]
print(f"First Smallest Positive Missing Number In Array {nums} is:\t", sol.firstMissingPositive(nums))