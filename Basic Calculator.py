def add(x, y):
  """Adds two numbers"""
  return x + y

def subtract(x, y):
  """Subtracts two numbers"""
  return x - y

def multiply(x, y):
  """Multiplies two numbers"""
  return x * y

def divide(x, y):
  """Divides two numbers"""
  if y == 0:
    return "Cannot divide by zero"
  else:
    return x / y

while True:
  print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

  choice = input("Enter choice(1/2/3/4/5): ")

  if choice in ('1', '2', '3', '4'):
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
    print("Exiting program.")
    break
  else:
    print("Invalid input")

print("Thank you for using the calculator!")
