def design():
    str1 = "      "
    str2 = "*"
    for i in range(1, 6):
        print(str1 + (str2 * i) + str1)
        str1 = slice(0, len(str1) - 2, 1)


if __name__ == "__main__":
    design()
