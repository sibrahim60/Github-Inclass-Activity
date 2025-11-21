def simple_calc():
    # 1. Get numbers and operation
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *): ")
    num2 = float(input("Enter second number: "))

    # 2. Perform calculation
    if operation == '+':
        print(f"Result: {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1 * num2}")
    else:
        print("Invalid operation entered.")

    # Run the simple calculator
simple_calc()

