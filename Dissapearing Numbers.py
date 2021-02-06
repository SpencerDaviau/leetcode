#5 Minutes
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #Create missing numbers list
        missingNums = []
        
        #For all indexes in nums
        for i in nums:
            #Position is equal to index -1
            pos = abs(i) - 1 
            #Position is > 0 then multiply and equal the index -1
            if nums[pos] > 0:
                nums[pos] *= -1
            
        #For all indexes in the range of length nums
        #We check if i is > 0 because if it is its a missing number
        #Therefore we append it to the missingNums List and Return the answer
        for i in range(len(nums)):
            if nums[i] > 0:
                missingNums.append(i + 1)
                
        return missingNums

