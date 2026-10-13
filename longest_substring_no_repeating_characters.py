class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        longest_sub = 0
        actual_sub = 0

        substring = []

        for c in s:
            if c not in substring:
                substring.append(c)
                actual_sub += 1
            
            elif c in substring:
                valid_substring = False
                if actual_sub > longest_sub:
                    longest_sub = actual_sub
                while valid_substring == False: 
                    ch = substring[0]
                    if ch == c:
                        substring.remove(ch)
                        actual_sub -= 1
                        valid_substring = True
                    else:
                        substring.remove(ch)
                        actual_sub -= 1
                substring.append(c)
                actual_sub += 1
            
        if actual_sub > longest_sub:
            longest_sub = actual_sub
        
        return longest_sub
                




                