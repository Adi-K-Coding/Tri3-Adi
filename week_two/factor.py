class Factor:
    # constructor
    def __init__(self):
        self.factor_seq = []

    # factors method using class and call function

    def __call__(self, n):
        print("Printing Factors of", n, " using call function... ")
        for i in range(1, n + 1):
            if n % i == 0:
                self.factor_seq.append(i)
        for j in self.factor_seq:
            if j == n:
                print(j, end=" ")
            else:
                print(j, end=" , ")
        self.factor_seq.clear()
        return ""


# factors imperatively
def normal_factor():
    n = int(input("What number do you want the factors for"))
    print(" ")
    print("Printing Factors of", n, "in imperative... ")
    for i in range(1, n + 1):
        if n % i == 0:
            if i == n:
                print(i, end="")
            else:
                print(i, end=", ")

    print("")


# test cases for class call
def runner_call():
    factor_of = Factor()  # object instantiation and run __init__ method
    print(factor_of(4))
    print(factor_of(1))
    print(factor_of(84))
    print(factor_of(12))
    print(factor_of(49))
    print(factor_of(33))
    print(factor_of(2048))


# test cases for imperative function
def runner_imperative():
    normal_factor(4)
    normal_factor(1)
    normal_factor(84)
    normal_factor(12)
    normal_factor(49)
    normal_factor(33)
    normal_factor(2048)


if __name__ == "__main__":
    runner_call()
    runner_imperative()
