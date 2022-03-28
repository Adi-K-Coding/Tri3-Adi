def swapper():
    int1 = input("Enter a number")
    int2 = input("Enter another number")
    print("Before Swap " + int1, int2)
    x1 = int1
    int1 = int2
    int2 = x1
    print("After Swap " + int1, int2)

    return int1, int2
