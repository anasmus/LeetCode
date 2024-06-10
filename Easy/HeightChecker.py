class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        difference = 0
        for index, height in enumerate(heights):
            if height != expected[index]:
                difference += 1

        return difference
