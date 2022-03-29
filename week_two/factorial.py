class Factorial:
    def __init__(self):
        self.factorialSeq = []

    def __call__(self, n):
        if n < 2:
            self.factorialSeq.append(1)
            for i in self.factorialSeq:  # Breaks out of the loop if n is less than one
                if i == 1:
                    print(i, end=" = ")
                else:
                    print(i, end=" x ")
            return 1
        else:
            # Compute the requested Factorial number
            self.factorialSeq.append(n)  # builds list
        return n * self(n - 1)


def factorial_function():
    n = int(input("What number would you like to factorial"))
    facto_of = Factorial()  # object instantiation and run __init__ method
    print(facto_of(n))


if __name__ == "__main__":
    factorial_function()
