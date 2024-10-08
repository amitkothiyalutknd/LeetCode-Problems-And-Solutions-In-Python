# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

class Solution:
    def combinationSum(self, candidates, target):
        combination, current = [], []

        self.generateCombinations(0, candidates, current, combination, target)

        return combination

    def generateCombinations(self, i, candidates, current, combination, target):
        if target < 0:
            return
        
        if target == 0:
            combination.append(current[:])

        for j in range(i, len(candidates)):
            current.append(candidates[j])
            self.generateCombinations(j, candidates, current, combination, target - candidates[j])
            current.pop()  # backtrack to avoid duplicate solutions

sol = Solution()
candidates = list(map(int, input("Enter The Candidates Values Inside A list. Separate Each Inputs from Single Space.: ").split(' ')))
target = int(input("Enter The Target Fot Those Have To Generate Sum Combination:\t"))
print(f"The Output Combination List is {sol.combinationSum(candidates, target)} From The Candidates List {candidates} To Form The Sum Combinations Of Number {target}. ")