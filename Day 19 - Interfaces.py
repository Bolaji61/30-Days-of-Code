class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.n = n
        total = 0
        for i in range(n+1):
            try: 
                if n%i==0:
                    total = total + i
            except ZeroDivisionError as e:  #catch error that occurs when divisor, i==0.
                pass
        return total




n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
