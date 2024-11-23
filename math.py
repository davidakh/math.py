# Prompt user for an equation
equation = input("What do you want to solve? ")

# Check if the input matches the addition format
if "+" in equation:
    try:
        # Split the equation into parts
        x, y = equation.split("+")
        # Convert the parts to numbers and perform addition
        result = float(x.strip()) + float(y.strip())
        print(f"The answer is: {result}")
    except ValueError:
        # Handle invalid numbers
        print("math.py can currently only solve addition problems.")
else:
    print("math.py can currently only solve addition problems.")