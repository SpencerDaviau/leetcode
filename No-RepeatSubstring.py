def non_repeat_substring(str1):
    wStart = 0
    maxLength = 0
    CharAtIndex = {}

    for wEnd in range(len(str1)):
        rChar = str1[wEnd]
        if rChar in CharAtIndex:
            wStart = max(wStart, CharAtIndex[rChar] + 1)
        CharAtIndex[rChar] = wEnd
        maxLength = max(maxLength, wEnd-wStart + 1)
    return maxLength
