words = ["cool", "lock", "cook"]

mainCount = {}
result = []
for word in words:
    countDict = {}
    for letter in word:
        countDict[letter] = 1 if not countDict.get(letter) else countDict[letter] + 1
    if not mainCount:
        mainCount = countDict.copy()
    else:
        for letter, count in mainCount.items():
            if not countDict.get(letter):
                mainCount[letter] = 0
            else:
                mainCount[letter] = min(countDict[letter], count)

for letter, count in mainCount.items():
    result.extend([letter] * count)

print(result)
