class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        current_count = 0

        if len(s) == 1:
            return 1
        if len(set(s)) == 2:
            return 2
        l = 0
        seen = set()
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring