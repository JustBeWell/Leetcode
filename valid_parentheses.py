class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sequence = []

        closing_tags = ")]}"
        opening_tags = "{(["

        for c in s:
          if c in closing_tags and len(sequence) == 0:
            return False

          if c in opening_tags:
            sequence.append(c)
          
          if c in closing_tags:
            first_closing_option = sequence[len(sequence)-1]
            if first_closing_option == "(" and c == ")":
              sequence.pop()
            elif first_closing_option == "[" and c == "]":
              sequence.pop()
            elif first_closing_option == "{" and c == "}":
              sequence.pop()
            else:
              return False
        
        if len(sequence) != 0:
          return False
        else:
          return True

        



          

          

          

          