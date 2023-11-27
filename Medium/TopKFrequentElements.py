class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}
        for num in nums:
            if numsCount.get(num) is not None:
                numsCount[num] += 1
            else:
                numsCount[num] = 1

        output = list(numsCount.keys())
        output.sort(key=lambda num: numsCount[num], reverse=True)
        output = output[0:k]

        return output
