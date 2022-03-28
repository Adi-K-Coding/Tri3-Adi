from pip._internal.utils.misc import tabulate


def multi_table():
    u_input = input("Enter a number between 10 and 99: ")
    num1 = int(u_input[0])
    num2 = int(u_input[1])
    for i in range(1, 10):
        num1multiplied = num1*i
        num2multiplied = num2*i
        num1multiplied_string = str(num1multiplied)
        num2multiplied_string = str(num2multiplied)
        if len(num1multiplied_string) == 1:
            num1multiplied = "0"+num1multiplied_string
        if len(num2multiplied_string) == 1:
            num2multiplied = "0"+num2multiplied_string
        print(num1multiplied, end=" | ")
        print(num2multiplied, end=" | ")
        # first two rows printed, both are ints currently
        num2multiplied_one = str(num2multiplied)[0]
        num2multiplied_two = str(num2multiplied)[1]
        x = int(num1multiplied)
        y = int(num2multiplied_one)
        row_three = x+y
        row_three_expression = ""
        row_three_string = str(row_three)
        print(row_three, end=" | ")
        print(row_three_string+num2multiplied_two, end=" | ")
        print(" ")


if __name__ == "__main__":
    multi_table()
