from operations import Arithmetic_Operations,Scientific
#user prompt
opt=int(input("Enter 1 if you want to perform arithmetic operation\t2 if you want to perform scientific"))
if(opt==1):
    a=float(input("Enter first number"))
    b=float(input("Enter second Number"))

    choice=int(input("Input 1 to add\nInput 2 to subtract\nInput 3 to multiply\nInput 4 to divide "))
    at=Arithmetic_Operations()
    if choice==1:
        at.addition(a,b)
    elif choice==2:
        at.subtraction(a,b)
    elif choice==3:
        at.multiply(a,b)
    elif choice==4:
        at.division(a,b)
    else:
        print("Invalid Input")
elif(opt==2):
    a=float(input("Enter the number"))
    choice=int(input("Input 1 to use Sin\t2 to use cosine"))
    st=Scientific()
    if choice==1:
        st.sin(a)
    elif choice==2:
        st.cos(a)
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice")

import math
class Arithmetic_Operations:
    def addition(self,a,b):
        print(f"{a+b} is the sum of the given numbers")
    def subtraction(a,b):
        print(f"{a-b} is the difference of the given numbers")

    def multiply(self,a,b):
        print(f"{a*b} is the product of the given numbers")

    def division(self,a,b):
        try:
            print("Second Number cant be zero")
        except:
            print(f"{a/b} is the quotient of the given numbers")

class Scientific():
    def sin(self,a):
        print(math.sin(a))
    def cos(self,a):
        print(math.cos(a))