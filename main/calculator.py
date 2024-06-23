class Calculator:
    def __init__(self) -> None:
        self.calc_on = True

    def calculate(self):
        def check_valid():
            for c in term:
                if c not in '0123456789+-*/. ':
                    print(False)
                    calc.calculate()
        while self.calc_on:
            term = input("calc> ")
            check_valid()
            if term == "* +":
                self.calc_on = False
            else:
                print(eval(term))


# Create an instance of the Calculator class
calc = Calculator()


# Call the calculate method on the instance
calc.calculate()
