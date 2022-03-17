def matrix1():
    matrix = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
              ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
              ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
              ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']]
    print("Printing keyboard...")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
