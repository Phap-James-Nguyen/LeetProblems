class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        strin = ""

        # any number divisible by 15 can divide by 3 and 5
        #The result array length is the same as n
        # multiple of 3 is Fizz, multiple of 5 is Buzz, multiple of both is FIzzBuzz
        # all others are just normal numbers

        for i in range(n):
            if((i+1) % 15 == 0):
                strin = "FizzBuzz"
            elif((i+1) % 5 == 0):
                strin = "Buzz"
            elif((i+1) % 3 == 0):
                strin = "Fizz"
            else:
                strin = str((i+1))

            result.append(strin)


        return result

        