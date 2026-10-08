class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            current_count = r - l + 1
            longest_substring = max(longest_substring, current_count)

        return longest_substring