class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = "" # 5Hello5World
        for i in strs:
            result_string += str(len(i)) + "#" + i
        print(result_string)
        return result_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res