class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
          return False
          
        first_word = set()
        second_word = set()

        for c in s:
          first_word.add(c)
        
        for c in t:
          second_word.add(c)
        
        if len(first_word.intersection(second_word)) != len(first_word) :
          return False
        
        first_word_occurences_map = {}

        for c in s:
          if c in first_word_occurences_map:
            first_word_occurences_map[c] += 1
          else:
            first_word_occurences_map[c] = 1
        
        second_word_occurences_map = {}

        for c in t:
          if c in second_word_occurences_map:
            second_word_occurences_map[c] += 1
          else:
            second_word_occurences_map[c] = 1
        
        for k in first_word_occurences_map:
          if second_word_occurences_map[k] != first_word_occurences_map[k]:
            return False
        
        return True
          
      