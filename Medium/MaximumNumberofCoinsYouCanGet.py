class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        picks = len(piles) // 3
        index = 1
        piles.sort(reverse=True)
        coins = 0

        for i in range(picks):
            coins += piles[index]
            index += 2
        return coins
