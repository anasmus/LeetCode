hand = [1, 2, 3, 4, 5, 6]
groupSize = 2

totalHands = len(hand) // groupSize
if totalHands != len(hand) / groupSize:
    print(False)
    exit(1)

sortedHand = sorted(hand)

for i in range(totalHands):
    previousCard = sortedHand.pop(0)
    count = 1
    index = 0
    while count < groupSize:
        if previousCard + 1 == sortedHand[index]:
            count += 1
            previousCard = sortedHand.pop(index)
            index -= 1
        index += 1
        if sortedHand and index == len(sortedHand):
            print(False)
            exit(1)

print(len(sortedHand) == 0)
