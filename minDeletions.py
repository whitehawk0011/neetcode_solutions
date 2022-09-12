# Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# https://leetcode.com/submissions/detail/798265335/
'''
first used hashmap to store character frequencies
then counted number of characters and stored them in array
then checked if they were in decreasing order strictly
or else made them by decreasing them by one in each index than the previous
'''


class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        values =[]
        for i in count.values():
            values.append(i)
        values.sort()
        initial = count.values()
        print (values)
        difference = 0
        index = len(values)-2
        last_index_num = values[len(values)-1]
        while (index>=0):
            if values[index]<last_index_num:
                last_index_num = values[index]    
            else:
                values[index] = last_index_num - 1
                if values[index] <0:
                    values[index] =0
                last_index_num = values[index]               
            index=index-1

        difference = sum(initial)-sum(values)
        print(values)
        print(initial)
        return difference
        
        
        

            
        
        
