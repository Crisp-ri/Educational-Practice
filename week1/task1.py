import this

# 1. Declare variables іof different types
print("1. VARIABLE DECLARATIONS")

# Integer type variables
int_var1 = 10
int_var2 = 25
int_var3 = -15

print(f"Integer variables:")
print(f"  int_var1 = {int_var1}")
print(f"  int_var2 = {int_var2}")
print(f"  int_var3 = {int_var3}")

# Float type variables
float_var1 = 3.14
float_var2 = 2.71828
float_var3 = -9.87

print(f"\nFloat variables:")
print(f"  float_var1 = {float_var1}")
print(f"  float_var2 = {float_var2}")
print(f"  float_var3 = {float_var3}")

# String type variables
str_var1 = "Hello, Python!"
str_var2 = "World"
str_var3 = "Programming"

print(f"\nString variables:")
print(f"  str_var1 = '{str_var1}'")
print(f"  str_var2 = '{str_var2}'")
print(f"  str_var3 = '{str_var3}'")

# 2. Test arithmetic operations
print("\n\n2. ARITHMETIC OPERATIONS")

print("\nAddition:")
print(f"  {int_var1} + {int_var2} = {int_var1 + int_var2}")
print(f"  {float_var1} + {float_var2} = {float_var1 + float_var2}")
print(f"  {int_var1} + {float_var1} = {int_var1 + float_var1}")

print("\nSubtraction:")
print(f"  {int_var2} - {int_var1} = {int_var2 - int_var1}")
print(f"  {float_var2} - {float_var1} = {float_var2 - float_var1}")
print(f"  {int_var2} - {float_var1} = {int_var2 - float_var1}")

print("\nMultiplication:")
print(f"  {int_var1} * {int_var2} = {int_var1 * int_var2}")
print(f"  {float_var1} * {float_var2} = {float_var1 * float_var2}")
print(f"  {int_var1} * {float_var1} = {int_var1 * float_var1}")

print("\nDivision:")
print(f"  {int_var2} / {int_var1} = {int_var2 / int_var1}")
print(f"  {float_var2} / {float_var1} = {float_var2 / float_var1}")
print(f"  {int_var2} / {float_var1} = {int_var2 / float_var1}")

print("\nInteger Division (//):") 
print(f"  {int_var2} // {int_var1} = {int_var2 // int_var1}")

print("\nModulo (%):")
print(f"  {int_var2} % {int_var1} = {int_var2 % int_var1}")

# 3. String operations
print("\n\n3. STRING OPERATIONS")

print(f"\nConcatenation:")
print(f"  '{str_var1}' + ' ' + '{str_var2}' = '{str_var1} {str_var2}'")

print(f"\nString repetition:")
print(f"  '{str_var2}' * 3 = '{str_var2 * 3}'")

# 4. Interactive input
print("\n\n4. INTERACTIVE INPUT")

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))
user_height = float(input("Enter your height in meters: "))

print(f"\nYou entered:")
print(f"  Name: {user_name}")
print(f"  Age: {user_age}")
print(f"  Height: {user_height}")

print(f"\nCalculated values:")
print(f"  Next year you will be {user_age + 1} years old")
print(f"  Your height in cm: {user_height * 100}")

# 5. Type information
print("\n\n5. TYPE INFORMATION")

print(f"\nVariable types:")
print(f"  type({int_var1}) = {type(int_var1)}")
print(f"  type({float_var1}) = {type(float_var1)}")
print(f"  type('{str_var1}') = {type(str_var1)}")

# 6. Comparison with Bash
print("\n\n6. PYTHON VS BASH COMPARISON")
comparison = """
PYTHON vs BASH SYNTAX DIFFERENCES:

1. VARIABLE DECLARATION:
   Python:  my_var = 10
   Bash:    my_var=10

2. DATA TYPES:
   Python:  Dynamically typed, explicit type support
   Bash:    Everything is a string by default

3. PRINT/ECHO:
   Python:  print("Hello")
   Bash:    echo "Hello"

4. INPUT:
   Python:  name = input("Enter name: ")
   Bash:    read -p "Enter name: " name

5. ARITHMETIC:
   Python:  result = 10 + 5
   Bash:    result=$((10 + 5)) or result=$(expr 10 + 5)

6. COMMENTS:
   Python:  # This is a comment
   Bash:    # This is a comment

7. STRING CONCATENATION:
   Python:  "Hello " + "World"
   Bash:    "Hello $world" or "Hello ""World"

8. CONTROL STRUCTURES:
   Python:  if x > 5:
            vs (no parentheses required, uses colons and indentation)
   Bash:    if [ $x -gt 5 ]; then

9. LOOPS:
   Python:  for i in range(5):
   Bash:    for i in {1..5} or for ((i=1; i<=5; i++))

10. FUNCTION CALLS:
    Python:  len(string)
    Bash:    ${#string}
"""
print(comparison)

