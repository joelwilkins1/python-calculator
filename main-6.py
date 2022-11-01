#Joel Wilkins
#03/08
#calculator program





print('#### Welcome to the calculator ####')
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def powerof(x,y):
    return x**y

def square(x,y):
    return x*y


print("What calculation would you like to do? ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power of")
print("6.Square")

while True:
    
    choice = input("Enter choice(1/2/3/4/5/6): ")

    
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        

        elif choice == '5':
            print(num1, '**', num2, '=', (num1**num2))


        elif choice == '6':
            print(num1, '*', num2, '=', square(num1,num2))


          
        next_calculation = input("Do another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")





  
  