# Module calculator
# Addition, SUbstraction, Multiplication, Division
# Division: User dividend 0-> You cannot enter zero

def add(a,b):
    return a + b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "You cannot enter zero"
    return a/b

def calculator():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", add(a,b))
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", sub(a,b))
    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", mul(a,b))
    elif choice == 4:
        a = int(input("Enter dividend: "))
        b = int(input("Enter divisor: "))
        print("Result: ", div(a,b))
    else:
        print("Invalid choice")
calculator()



