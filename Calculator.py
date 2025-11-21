def simple_calc():
    
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *): ")
    num2 = float(input("Enter second number: "))

    
    if operation == '+':
        print(f"Result: {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1 * num2}")
    else:
        print("Invalid operation entered.")


simple_calc()
