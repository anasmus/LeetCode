class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[-1])
        prefixSum = [sum % k for sum in prefixSum]

        hashMap = {}
        for sum in prefixSum:
            if sum == 0:
                count += 1
            if hashMap.get(sum) is None:
                hashMap[sum] = 1
            else:
                count += hashMap[sum]
                hashMap[sum] += 1
        return count
