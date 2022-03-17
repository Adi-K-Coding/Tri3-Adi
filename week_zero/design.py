def design():
    treesize = input("How large would you like your tree to be:  ")
    treesizeint = int(treesize)
    print(" ")
    str1 = " " * treesizeint
    str2 = "* "
    for i in range(1, treesizeint):
        print(str1 + (str2 * i))
        str1 = str1[0: len(str1) - 1]

    spcs = " " * (treesizeint-2)

    print("", end="")
    print(spcs, end=" ||| ")
    print("")
    print("", end="")
    print(spcs, end=" ||| ")


if __name__ == "__main__":
    design()
