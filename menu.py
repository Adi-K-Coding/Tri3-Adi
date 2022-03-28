from week_zero.swapper import swapper
from week_zero.matrix import matrix1
from week_zero.design import design
from week_zero.funcy import monkey
from week_one.week_one import fibonacci
from week_one.week_one import for_loopy, while_loopy, recursive_loopy
from main import my_info
from week_two.factor import normal_factor
from week_two.Palindrome import runner1
from week_two.factorial import factorial_function

main_menu = [
    ["About Me", my_info],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swap", swapper],
    ["Factorial", factorial_function],
    ["Factor", normal_factor],
    ["Palindrome", runner1],
    ["Fibonacci", fibonacci],
]

week_two_sub_menu = [
    ["InfoDB For Loop", for_loopy],
    ["InfoDB While Loop", while_loopy],
    ["InfoDB Recursive Loop", recursive_loopy],
]

week_three_sub_menu = [
    ["Matrix", matrix1],
    ["Design", design],
    ["Animation", monkey],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    print("")
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Number Functions", submenu])
    menu_list.append(["Looping Fun", week2_submenu])
    menu_list.append(["Function Fun", week3_submenu])
    buildMenu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()




def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)


def week2_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week_two_sub_menu)


def week3_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week_three_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")
    print(" ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
