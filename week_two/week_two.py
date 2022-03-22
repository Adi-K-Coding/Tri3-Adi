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
    "Players": ["Jan Oblak", "Antoine Griezmann", "João Félix", "Luis Suárez"]
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
    "City": "Bangalore ",
    "Team Name": "Royal Challengers Bangalor",
    "Stadium": "M Chinnaswamy Stadium",
    "Players": ["Virat Kohli", "Faf du Plessis", "Glenn Maxwell", "Josh Hazelwood"]
})


def data(n):
    print("Country: ", InfoDb[n]["Country"], "\nLeague: ", InfoDb[n]["League"],
          "\nCity: ", InfoDb[n]["City"], "\nTeam Name: ", InfoDb[n]["Team Name"],
          "\nStadium: ", InfoDb[n]["Stadium"])  # using comma puts space between values
    print("\n", "Players: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Players"]))  # join allows printing a string list with separator
    print()


def for_loopy():
    for i in range(len(InfoDb)):
        data(i)


def while_loopy(x):
    while x < len(InfoDb):
        data(x)
        x += 1
    return


def recursive_loopy(x):
    if x < len(InfoDb):
        data(x)
        recursive_loopy(x + 1)
    return


def fibonacci(input1):
    try:
        if input1 < 2:
            raise ValueError
        print(0)
        current_number = 1
        print(current_number)
        fibonacci1((input1 - 2), 0, 1)
    except ValueError:
        print("Please enter a valid input")


def fibonacci1(number_times, prev_number, current_number):
    temp = current_number
    current_number = current_number + prev_number
    print(current_number)
    prev_number = temp
    if number_times > 0:
        fibonacci1(number_times - 1, prev_number, current_number)


if __name__ == "__main__":
    print("1--For Loop")
    print("2--While Loop")
    print("3--Recursive Loop")
    try1 = input("What type of loop do you want?")
    print(" ")
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
