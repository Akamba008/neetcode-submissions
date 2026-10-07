class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = 0
        length = 0

        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                word = s[j + 1 : j + length + 1]
                decoded.append(word)
                j += 1 + length
                i = j    
            else:
                j += 1
        return decoded