class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        maxCount = 0

        while numSet:
            num = numSet.pop()
            count = 1

            currentNum = num - 1
            while currentNum in numSet:
                count += 1
                numSet.discard(currentNum)
                currentNum -= 1

            currentNum = num + 1
            while currentNum in numSet:
                count += 1
                numSet.discard(currentNum)
                currentNum += 1
            
            maxCount = max(maxCount, count)
        
        return maxCount