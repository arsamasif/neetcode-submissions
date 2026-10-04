class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in anagrams_dict:
                anagrams_dict[sorted_i].append(i)
            else:
                anagrams_dict[sorted_i] = [i]

        return list(anagrams_dict.values())