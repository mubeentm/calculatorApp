import math
def add():
    a = int(input("Enter value for a :"))
    b = int(input("Enter the value for b :"))
    return a + b

def subtract():
    a = int(input("Enter value for a :"))
    b = int(input("Enter the value for b :"))
    return a - b

def multiply():
    a = int(input("Enter value for a :"))
    b = int(input("Enter the value for b :"))
    return a * b

def divide():
    a = int(input("Enter value for a :"))
    b = int(input("Enter the value for b :"))
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"
def percentag():
    a=int(input("Enter the no. : "))
    percent=int(input("Enter the percentage : "))
    return (a*percent)/100

def square_root():
    a = int(input("Enter value :"))
    import math
    return math.sqrt(a)

def power():
    a = int(input("Enter value for a :"))
    b = int(input("Enter the value for b :"))
    return a ** b

print("Enter the option \n1.Add\n2.Substract\n3.Multiply\n4.Division")
n= int(input("Enter the option : " ))
while(True):
    if n == 1:
        add()
    elif n==2:
        subtract()
    elif n==3:
        divide()
    elif n==4:
        percentag()
    elif n==5:
        square_root()
    elif n==6:
        power()
    else:
        print("invalid option")
        break

