class Operations:
    def __init__(self, value):
        self.value = value

    def add(self, num):
        return self.value + num

    def subtract(self, num):
        return self.value - num

    def multiply(self, num):
        return self.value * num

    def divide(self, num):
        if num == 0:
            return "Cannot divide by zero"  
        return self.value / num
    
user_value = int(input("Enter a number: "))
calculator = Operations(user_value)
print("Addition:", calculator.add(5))
print("Subtraction:", calculator.subtract(5))
print("Multiplication:", calculator.multiply(5))
print("Division:", calculator.divide(5))

