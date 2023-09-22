# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        subString = str()
        stringList = []
        for char in inputString:
            if char not in subString:
                subString += char
            else:
                if char == subString[0]:
                    subString = subString[1::]
                    subString += char
                else:
                    subString = str()
                    subString += char
            stringList.append(subString)
        subString = max(stringList, key = len, default = 0)
        print(f"The Length of Longest Substring:'{subString}' From The InputString:'{inputString}' Is -> {len(subString)}.")

solObject = Solution()
inputString = str(input("Enter The String As Input: "))
solObject.lengthOfLongestSubstring(inputString)