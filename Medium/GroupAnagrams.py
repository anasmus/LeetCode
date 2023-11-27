class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sortedString = str(sorted(string))
            if groups.get(sortedString) is not None:
                groups.get(sortedString).append(string)
            else:
                groups[sortedString] = [string]
        output = []
        for group in groups.values():
            output.append(group)

        return output
