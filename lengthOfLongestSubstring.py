class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxstringlen = 0
        tempstring = ""
        if len( s ):
            tempstring=tempstring +s[0]
            tempstringlen = 1
            maxstringlen += 1

        for i in range( 1, len( s ) ):
            m= s[i]
            try:
                culprit_index = tempstring.index(m)
                tempstring = tempstring[culprit_index+1:tempstringlen]
                tempstringlen = len(tempstring)
                tempstringlen = tempstringlen +1
            except :

                tempstringlen += 1
                maxstringlen = max( tempstringlen, maxstringlen )
                right += 1
                pass
            tempstring=tempstring +m

        return maxstringlen
      
      #check why i did try catch , index of was not used . culprit index needs to be revised
      #https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
