class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        seen = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if seen.get(remaining) is not None:
                output.append(seen.get(remaining))
                output.append(index)
                break
            else:
                seen[num] = index
        return output
