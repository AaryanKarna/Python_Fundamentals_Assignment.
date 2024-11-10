#Aaryan Karn
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "The number cannot be zero"
    return x/y

def calculator():
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    choice = input("Enter your choice:")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 'a':
        result=add(num1,num2)
        print("The result is: ",result)
    elif choice == 'b':
        result=sub(num1,num2)
        print("The result is: ",result)
    elif choice == 'c':
        result=multiply(num1,num2)
        print("The result is: ",result)
    elif choice == 'd':
        result=divide(num1,num2)
        print("The result is: ",result)

calculator()



    