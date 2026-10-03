class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}

        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in string_map:
                string_map[sorted_str].append(i)
            else:
                string_map[sorted_str] = [i]

        return list(string_map.values())