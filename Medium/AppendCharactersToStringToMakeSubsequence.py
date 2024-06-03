class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        prefixCount = 0
        sIndex, tIndex = 0, 0
        sLength, tLength = len(s), len(t)

        while sIndex < sLength and tIndex < tLength:
            if s[sIndex] == t[tIndex]:
                prefixCount += 1
                tIndex += 1
            sIndex += 1

        return tLength - prefixCount
