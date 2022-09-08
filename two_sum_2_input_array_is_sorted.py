class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_of_time = 0
        last_one = -1
        for i in range (0,len(numbers)):
            if (i==0):
                last_one = numbers[i]
               
            else:
                if (numbers[i] == last_one):
                    number_of_time = number_of_time +1
                else:
                    last_one = numbers[i]
                    number_of_time = 0
            
            
            limit = True
            j= i+1
            if (number_of_time ==0):
                while ((limit == True) and (j <len(numbers))):
                    
                    if numbers[i]+numbers[j] > target:
                            limit = False
                    if numbers[i]+numbers[j] == target:
                        return [i+1,j+1]
                    j = j+1
        return []
        
        #dont count the already processed number , when the addition exceeds the target , dont go through the second loop
        #https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
        #contributor- shub
