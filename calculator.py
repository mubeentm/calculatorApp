def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"
a=int(input("Enter value for a :"))
b = int(input("Enter the value for b :"))
print("Enter the option \n1.Add\n2.Substract\n3.Multiply\n4.Division")
n= int(input("Enter the option : " ))
while(True):
    if n == 1:
        add(a,b)
    elif n==2:
        subtract(a,b)
    elif n==3:
        divide(a,b)
    else:
        print("invalid option")
        break
