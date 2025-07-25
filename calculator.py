#We are going to create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division) and the operation based on the user's input and print the result.
float1 = float(input("Enter first number: "))
float2 = float(input("Enter second number: "))

sum_result = float1 + float2
sub_result = float1 - float2
mul_result = float1 * float2
div_result = float1 / float2 if float2 != 0 else "undefined (division by zero)"

print(f"Sum: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")