class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count the length of the last word
        while i >= 0 and s[i] != " ":
            result += 1
            i -= 1

        return result


        
        


