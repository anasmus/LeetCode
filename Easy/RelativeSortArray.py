class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr2:
            count[num] = 0

        sortedArray = []
        finalArray = []
        
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                sortedArray.append(num)

        sortedArray.sort()
        
        for num, numCount in count.items():
            finalArray += [num] * numCount

        return finalArray + sortedArray        