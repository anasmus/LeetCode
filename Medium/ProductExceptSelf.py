from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, result = [], [], []
        numsLength = len(nums)

        for num in nums:
            prefix.append(num if len(prefix) == 0 else num * prefix[-1])

        for num in nums[::-1]:
            suffix.append(num if len(suffix) == 0 else num * suffix[-1])
        suffix.reverse()

        for i in range(numsLength):
            previousProd = prefix[i - 1] if i - 1 >= 0 else 1
            nextProd = suffix[i + 1] if i + 1 < numsLength else 1
            result.append(previousProd * nextProd)

        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
