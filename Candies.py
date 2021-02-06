'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyList = []
        maxCandy = max(candies)
    
        for num in candies:
            if num + extraCandies >= maxCandy:
                candyList.append(True)
            else:
                candyList.append(False)
        
        return candyList
'''