class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        word1 = strs[0]
        lengths = [len(s) for s in strs]
        for letter, char in enumerate(word1[0 : min(lengths)]):
            included =  False
            for word in strs[1:]:
                if char == word[letter]:
                    included = True
                else:
                    return prefix
            if included:
                prefix += char
        return prefix