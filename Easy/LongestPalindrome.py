class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = dict()
        for letter in s:
            hashMap[letter] = 1 if not hashMap.get(letter) else hashMap[letter] + 1

        doubles = 0

        for count in hashMap.values():
            doubles += count // 2

        palindromeLength = doubles * 2

        if palindromeLength != len(s):
            palindromeLength += 1

        return palindromeLength
