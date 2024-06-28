def lower(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("* ", end="")
        print("")

def upper(n):
    for i in range(0, n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0, n-i):
            print("*", end="")
        print("")

def pyramid(n):
    for i in range(0, n):
        for j in range(n-i, 1, -1):
            print(" ", end="")
        for j in range(0, i+1):
            print("* ", end="")
        print("")

if __name__ == "__main__":
    n = int(input("Enter n : "))
    print("\nLower Triangular : ")
    lower(n)
    print("\nUpper Triangular : ")
    upper(n)
    print("\nPyramid : ")
    pyramid(n)
