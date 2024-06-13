class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        index = 0
        for num, numCount in enumerate(count):
            for i in range(numCount):
                nums[index] = num
                index += 1
