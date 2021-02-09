def longest_substring_with_k_distinct(str1, k):

    wStart = 0
    maxLength = 0
    freq = {}

    for wEnd in range(len(str1)):
        rChar = str1[wEnd]
        if rChar not in freq:
            freq[rChar] = 0
        freq[rChar] += 1

        while len(freq) > k:
            lChar = str1[wStart]
            freq[lChar] -= 1
            if freq[lChar] == 0:
                del freq[lChar]
            wStart += 1
        maxLength = max(maxLength, wEnd-wStart + 1)
    return maxLength