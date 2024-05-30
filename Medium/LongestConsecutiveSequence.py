import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        lastNum = None
        totalCount, maxCount = 0, 0

        while len(nums) > 0:
            currentNum = heapq.heappop(nums)
            if lastNum is None:
                totalCount += 1
            elif lastNum + 1 == currentNum:
                totalCount += 1
            elif lastNum == currentNum:
                pass
            else:
                maxCount = max(maxCount, totalCount)
                totalCount = 1
            lastNum = currentNum

        maxCount = max(maxCount, totalCount)
        return maxCount
