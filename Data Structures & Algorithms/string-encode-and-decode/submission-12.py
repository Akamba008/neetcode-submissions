class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("^")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decoded = []
        while i < len(s):
            if s[i] == "^":
                length = int(s[j:i])
                decoded.append(s[i + 1 : i + length + 1])
                i += length + 1
                j = i
            else:
                i += 1
        return decoded

