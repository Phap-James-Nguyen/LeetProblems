class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        #use ord() function, which is a python ASCII function that returns ASCII characters
        # A = 65, so take that and subtract 64 = 1
        #if length of columnTitle is > 1, for every right letter it's add 26 from previous
        # This is like a base 26 number, for each digit you have to subtract 64 and then perform base 26 conversion
        # binary to decimal converstion ex:
        #111 = 7 -> (1*2^2) + (1 * 2^1) + (1 * 2^0)
        # A = 1 -> ((ord("A") - 64) * 26^0)
        # B = 2 -> ((ord("B") - 64) * 26^0)
        # AA = 27 ((ord("A") - 64) * 26^1) + ((ord("A") - 64) * 26^0)
        # AAA = 27 ((ord("A") - 64) * 26^2) + 27 ((ord("A") - 64) * 26^1) + ((ord("A") - 64) * 26^0)
        #else if columnTitle is 1 do return ord and minus 64

        result = 0
        power = 0
        i = len(columnTitle) - 1
        
        while i >= 0:
            result += (ord(columnTitle[i]) - 64) * (26**power)
            power = power + 1
            i = i -1

        return result
        