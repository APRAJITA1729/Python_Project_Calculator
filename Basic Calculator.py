# Basic Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply( x , y):
    return  x*y

def divide(x, y):
    if y == 0:
        return "Invalid input"
    return x/y


print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4):")

if choice == "1":
    x= float(input("Enter first number:"))
    y= float(input("Enter second number:"))
    print(f"Result:{add(x,y)}")

elif choice == "2" :
    x= float(input("Enter first number:"))
    y= float(input("Enter second number:"))
    print(f"Result:{subtract(x,y)}")
    
elif choice == "3":
    x= float(input("Enter first number:"))
    y= float(input("Enter second number:"))
    print(f"Result:{multiply(x,y)}")
elif choice == "4":
    x= float(input("Enter first number:"))
    y= float(input("Enter second number:"))
    print(f"Result:{divide(x,y)}")
else:
    print("This is basic Calculator. You can only add , subtract , multiply and divide of two numbers.")

