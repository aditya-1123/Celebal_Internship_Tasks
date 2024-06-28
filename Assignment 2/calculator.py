def add(x,y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if(y == 0): 
        return "cannot divide by 0"
    else:
        return x / y

print("Menu")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while(True):
    ch = int(input("\nChoose any of the above: "))
    if(ch < 5): 
        no1 = float(input("Enter no1: "))
        no2 = float(input("Enter no2: "))

        if(ch == 1): 
            print(f"{no1} + {no2} = {add(no1, no2)}") 
        elif(ch == 2): 
            print(f"{no1} - {no2} = {sub(no1, no2)}") 
        elif(ch == 3): 
            print(f"{no1} * {no2} = {mul(no1, no2)}",) 
        elif(ch == 4): 
            if(div(no1, no2) == "cannot divide by 0"): 
                print("cannot divide by 0")
            else: 
                print(f"{no1} / {no2} = {div(no1, no2)}")
    else: 
        print("Invalid Input")
