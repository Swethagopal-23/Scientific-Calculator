# Scientific-Calculator

**# Problem Statement**
Develop a scientific calculator with a variety of scientific functions such as sin, cos, tan, exponential, log, etc. You can use the built-in calculator on your Windows or Mac system as a reference for ideas. The design and functionality of your calculator are open to your interpretation.

**# Objective**
This Python program is a command-line scientific calculator that allows users to input and evaluate various mathematical expressions. The calculator supports a range of scientific functions, including trigonometric functions, exponential functions, logarithms, and basic arithmetic operations. The program continues to run, allowing multiple calculations, until the user decides to exit by typing "quit".

# Features
- **Trigonometric Functions**: `sin`, `cos`, and `tan` (assume input in degrees)
- **Exponential Function**: `exp`
- **Logarithmic Function**: `log`
- **Square Root Function**: `sqrt`
- **Mathematical Constants**: `pi`, `e`
- **Conversion Functions**: `degrees`, `radians`

# How It Works

1. **Import the Math Module**:
   - The program imports the Python `math` module, which provides the necessary mathematical functions and constants.

3. **Define Allowed Functions and Constants**: 
   - A dictionary comprehension is used to create a dictionary (`math_functions`) that includes all functions and constants from the `math` module, excluding special attributes (those starting with double underscores).
   - The dictionary is updated to convert trigonometric functions (`sin`, `cos`, `tan`) from degrees to radians before evaluation.

4. **Evaluate Expressions**: 
   - The `scientific_calculator` function takes a user-provided mathematical expression as input.
   - It uses the `eval` function to safely evaluate the expression using the `math_functions` dictionary, which restricts the evaluation to the defined safe functions and constants.
   - If the evaluation is successful, the result is returned. If an error occurs, the error message is returned.

5. **User Interaction Loop**:
   - The main part of the program runs an infinite loop, continuously prompting the user to enter a scientific expression.
   - If the user inputs "quit", the loop breaks, and the program exits.
   - Otherwise, the entered expression is evaluated, and the result is printed.
