{% include navigation.html %}

```python
import swapper
import matrix
import design
import funcy

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
