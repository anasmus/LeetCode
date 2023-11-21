class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateExists = False
        seen = {}
        for num in nums:
            if seen.get(num):
                duplicateExists = True
                break
            else:
                seen[num] = True
        return duplicateExists
