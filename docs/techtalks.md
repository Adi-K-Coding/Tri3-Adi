{% include navigation.html %}

### Week Three Accounts and Login Hacks
Hack One: Phone Number Added
![image](https://user-images.githubusercontent.com/34950822/162528328-224c1d8f-a931-4490-bf9b-873b4e5b4fef.png)
Hack Two: Added Logout and User Displayed on Page
![image](https://user-images.githubusercontent.com/34950822/162528568-23bd5ee7-7f91-4242-b98b-9d8076398105.png)
Hack Three: 





```python

from week_zero.week_zero_runner import design, funcy, swapper, matrix

main_menu = [
    ["swap", "swapper.py"],
    ["keyboard", "matrix.py"],
    ["design", "design.py"],
    ["animation", "funcy.py"],
    ["exit", "c"],
]

if __name__ == "__main__":
    while True:
        for i in range(len(main_menu)):
            print(main_menu[i][0])
        print("What would you like")
        userInput = input("")

        if userInput == "swap" or userInput == "1":
            int1 = input("Enter a number")
            int2 = input("Enter another number")
            print(" ")
            swapper.swapper(int1, int2)
        elif userInput == "keyboard" or userInput == "2":
            print(" ")
            matrix.matrix1()
        elif userInput == "design" or userInput == "3":
            print(" ")
            design.design()
        elif userInput == "animation" or userInput == "4":
            print(" ")
            funcy.monkey()
        elif userInput == "exit" or userInput == "5":
            exit()
        else:
            print("Enter a valid input")
        print("   ")
```

### Week One 

```python
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "Country": "United States",
    "League": "MLB",
    "City": "Los Angeles ",
    "Team Name": "Dodgers",
    "Stadium": "Dodger Stadium",
    "Players": ["Cody Bellinger", "Clayton Kershaw", "Trea Turner", "Mookie Betts", "Walker Buelher"]
})

InfoDb.append({
    "Country": "Spain",
    "League": "La Liga",
    "City": "Madrid ",
    "Team Name": "Atlético Madrid",
    "Stadium": "Wanda Metropolitano Stadium",
    "Players": ["Jan Oblak", "", "Antoine Griezmann", "João Félix", "Luis Suárez"]
})

InfoDb.append({
    "Country": "United States",
    "League": "NFL",
    "City": "Seattle ",
    "Team Name": "Seahawks",
    "Stadium": "Lumen Field",
    "Players": ["Jamal Adams", "Tyler Lockett", "Dk Metcalf", "Chris Carson", "Quandre Diggs"]
})

InfoDb.append({
    "Country": "India",
    "League": "IPL",
    "City": "Los Angeles ",
    "Team Name": "Dodgers",
    "Stadium": "M Chinnaswamy Stadium",
    "Players": ["Cody Bellinger", "Clayton Kershaw", "Trea Turner", "Mookie Betts", "Walker Buelher"]
})


def data(n):
    print("Country", InfoDb[n]["Country"], "\nLeague", InfoDb[n]["League"],
          "\nCity", InfoDb[n]["City"], "\nTeam Name", InfoDb[n]["Team Name"],
          "\nStadium", InfoDb[n]["Stadium"])  #printing all the values from the infoDB
    print("\t", "\nPlayers: ", end="") #end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Players"]))  # join allows printing a string list with separator, is useful here because "players"
    #is a list within the dictionary
    print()


def for_loopy():
    for i in range(len(InfoDb)):
        data(i)
#for loop

def while_loopy(x):
    while x < len(InfoDb):
        data(x)
        x += 1
    return
#while loop

def recursive_loopy(x):
    if x < len(InfoDb):
        data(x)
        recursive_loopy(x + 1)
    return
#recursive loop

def fibonacci(input1):
    try:# try catch used to detect only valid inputs for the length of the sequence
        if input1 < 2:
            raise ValueError
        print(0)
        current_number = 1
        print(current_number)
        fibonacci1((input1 - 2), 0, 1)
    except ValueError:
        print("Please enter a valid input")
#need a starter method to print first two values of fibonacci, then passes them into variables so the resursive math can be done

def fibonacci1(number_times, prev_number, current_number):
    temp = current_number
    current_number = current_number + prev_number
    print(current_number)
    prev_number = temp
    if number_times > 0:
        fibonacci1(number_times - 1, prev_number, current_number)
#fibonacci math using recursion

if __name__ == "__main__":
    print("1--For Loop")
    print("2--While Loop")
    print("3--Recursive Loop")
    try1 = input("What type of loop do you want?")
    if try1 == "1":
        print("From for loop: ")
        for_loopy()
    elif try1 == "2":
        print("From while loop: ")
        while_loopy(0)
    elif try1 == "3":
        print("From recursive loop: ")
        recursive_loopy(0)
    userInput = int(input("How many numbers should the fibonacci sequence be?"))
    print("Printing Fibonacci...")
    fibonacci(userInput)

```
### Week Two
#### Factor function
```python
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

```
#### Factorial Function
```python
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

```
#### Palindrome function
```python
import math


class Palindrome:
# call function
    def __call__(self, string):
        s = string.strip()
        palindrome1 = s.replace(" ", "").replace("!", "").replace(",", "").replace(".", "").replace("'", "").replace(
            "-", "").replace(":", "").replace(";", "").replace("?", "");
        palindrome = palindrome1.lower()
        # making all letters the same, getting rid of special characters
        print(palindrome)
        ispalindrome = True
        # function to check if string is palidrome
        lengthofinput = (len(palindrome) / 2) + 0.5
        for i in range(0, math.floor(lengthofinput)):
            if palindrome[i] != palindrome[len(palindrome) - (i + 1)]:
                ispalindrome = False
                break
        return ispalindrome;


def runner1():
    palindrome_of = Palindrome()  # object instantiation and run __init__ method
    # Test cases
    print(palindrome_of("ABA"))
    print(palindrome_of("ABBA"))
    print(palindrome_of("racecar"))
    print(palindrome_of("Was it a cat I saw?"))
    print(palindrome_of("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal - Panama"))
    print(palindrome_of("Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod."))
    print(palindrome_of("abcdefghijklmnopqrstuvwxyz"))
    print(palindrome_of("This is not a palendrome"))
    print(palindrome_of("This is close but not quite right etiuq ton tub esolc si sihT"))


if __name__ == "__main__":
    runner1()

```
