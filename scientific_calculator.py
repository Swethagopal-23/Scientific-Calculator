import math

def scientific_calculator(expression):
    
    # Define calculator_functions and constants
    calculator_functions = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    
    # Update calculator_functions to include some additional math functions
    calculator_functions.update({
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log,
        'sqrt': math.sqrt,
        'pi': math.pi,
        'e': math.e,
        'degrees': math.degrees,  
        'radians': math.radians   
    })
    
    # Evaluate the expression using the calculator_functions
    try:
        result = eval(expression, {"__builtins__": None}, calculator_functions)
        return result
    except Exception as e:
        return str(e)

# Example usage
if __name__ == "__main__":
    while True:
        exp = input("Enter a scientific expression (or 'quit' to exit): ")
        if exp.lower() == 'quit':
            break
        print("Result:", scientific_calculator(exp))
