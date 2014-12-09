__author__ = 'Deepak Nadig Anantha'


class ModulesOne:
    """
    A Skeleton Class for Future Use
    """

    def fib(n):  # write Fibonacci series up to n
        """
        Computes the Fibonacci Series up to 'n'
         :rtype : Prints a Fibonacci Series up to 'n'
        """
        a, b = 0, 1
        while b < n:
            print(b, ' ')
            a, b = b, a + b
        print()


    def fib2(n):  # return Fibonacci series up to n
        """
       Computes the Fibonacci Series up to 'n'
        :rtype : Returns a list 'result[]' that contains the fibonacci series
       """
        result = []

        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a + b
        return result