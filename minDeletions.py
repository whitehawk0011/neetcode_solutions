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
        
        
        

            
        
        
