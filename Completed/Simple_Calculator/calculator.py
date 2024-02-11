print(5*"*", "Simple Calculator", 5*"*")
print(29*"_")
def add(a,b):
  return a + b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b == 0: 
    return "Error: Division by zero."  
  return a/b

while True: 
  try: 
    op = int(input('Choose An Operation(1-ADD, 2-SUBTRACT, 3-MULTIPLY, 4-DIVIDE, 5-QUIT): '))
    if op == 5:
      print('Quitting Program')
      break
    num1 = float(input('number1: '))
    num2 = float(input('number2: '))
  except ValueError:
    print("Incorrect information entered.")
    continue
  else:
    if op == 1:
      print(f"  {num1}")
      print(f"+ {num2}")
      print(5*"_")
      print(" ",add(num1, num2), "\n")
    elif op == 2:
      print(f"  {num1}")
      print(f"- {num2}")
      print(5*"_")
      print(" ",subtract(num1,num2), "\n")
    elif op == 3:
      print(f"  {num1}")
      print(f"x {num2}")
      print(5*"_")
      print(" ",multiply(num1,num2), "\n")
    elif op ==  4:
      print(f"  {num1}")
      print(f"/ {num2}")
      print(5*"_")
      print(" ",divide(num1,num2), "\n")
    else:
      print("Error: Invalid Operator")
