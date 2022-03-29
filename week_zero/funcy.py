# funcy.py
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
MONKEY_COLOR = u"\u001b[33m"
RESET_COLOR = u"\u001B[0m\u001B[2D"


def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def monkey_print(position):
    print(ANSI_HOME_CURSOR)
    sp = " " * position
    print(MONKEY_COLOR, end="")
    print(sp + "     .\"`\".")
    print(sp + "  .-./ _=_ \\.-.")
    print(sp + " {  (,(oYo),) }}")
    print(sp + " {{ |   \"   |} }")
    print(sp + " { { \\(---)/  }}")
    print(sp + " {{  }'-=-'{ } }")
    print(sp + " { { }._:_.{  }}")
    print(sp + " {{  } -:- { } }")
    print(sp + " {_{ }`===`{  _}")
    print(sp + "((((\\)     (/))))")
    print(RESET_COLOR)


#     ."`".
#  .-./ _=_ \.-.
# {  (,(oYo),) }}
# {{ |   "   |} }
# { { \(---)/  }}
# {{  }'-=-'{ } }
# { { }._:_.{  }}
# {{  } -:- { } }
# {_{ }`===`{  _}
# ((((\)     (/))))

# ship function, iterface into this file
def monkey():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        monkey_print(position)  # call to function with parameter
        time.sleep(.1)


if __name__ == "__main__":
    monkey()