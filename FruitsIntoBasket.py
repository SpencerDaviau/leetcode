def fruits_into_baskets(fruits):
    wStart = 0
    maxLength = 0
    fruitFrequency = {}

    for wEnd in range(len(fruits)):
        rightFruit = fruits[wEnd]
        if rightFruit not in fruitFrequency:
            fruitFrequency[rightFruit] = 0
        fruitFrequency[rightFruit] += 1

        while len(fruitFrequency) > 2:
            leftFruit = fruits[wStart]
            fruitFrequency[leftFruit] -= 1
            if fruitFrequency[leftFruit] == 0:
                del fruitFrequency[leftFruit]
            wStart += 1
        maxLength = max(maxLength, wEnd - wStart + 1)
    return maxLength