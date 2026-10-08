class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}

        # Store indices for each character
        for i, val in enumerate(s):
            if val not in hashmap:
                hashmap[val] = []

            hashmap[val].append(i)

        longest = 0

        # Check each character
        for char in hashmap:
            indices = hashmap[char]

            l = 0

            for r in range(len(indices)):
                # Number of non-char characters between l and r
                length = indices[r] - indices[l] + 1
                char_count = r - l + 1
                gaps = length - char_count

                # Too many gaps, move left forward
                while gaps > k:
                    l += 1

                    length = indices[r] - indices[l] + 1
                    char_count = r - l + 1
                    gaps = length - char_count

                # Remaining replacements can extend the substring
                remaining_k = k - gaps

                total_length = length + remaining_k

                # Can't go past the size of the string
                total_length = min(total_length, len(s))

                longest = max(longest, total_length)

        return longest