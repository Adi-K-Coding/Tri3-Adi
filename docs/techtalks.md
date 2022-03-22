{% include navigation.html %}

```python

from week_zero import design, funcy, swapper, matrix

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
