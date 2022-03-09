def swapper(int1, int2):
    print("Before Swap " + int1, int2)
    if int1 >= int2:
        x1 = int1
        int1 = int2
        int2 = x1
    print("After Swap " + int1, int2)

    return int1, int2
