def number_to_string(num):
    
    # Handle special case of zero
    if num == 0:
        return "0"
    
    # Determine if number is negative
    is_negative = num < 0
    num = abs(num)
    
    # Handle float numbers
    if isinstance(num, float):
        # Convert to string manually by extracting digits
        # Split into integer and fractional parts
        integer_part = int(num)
        fractional_part = num - integer_part
        
        # Convert integer part
        result = ""
        if integer_part == 0:
            result = "0"
        else:
            temp = integer_part
            while temp > 0:
                digit = temp % 10
                result = chr(ord('0') + digit) + result
                temp //= 10
        
        # Convert fractional part (up to 10 decimal places)
        if fractional_part > 0:
            result += "."
            for _ in range(10):
                fractional_part *= 10
                digit = int(fractional_part)
                result += chr(ord('0') + digit)
                fractional_part -= digit
                if fractional_part == 0:
                    break
        
        # Add negative sign if needed
        if is_negative:
            result = "-" + result
        
        return result
    
    else:  # Handle integers
        result = ""
        temp = num
        
        while temp > 0:
            digit = temp % 10
            # Convert digit (0-9) to corresponding character ('0'-'9')
            result = chr(ord('0') + digit) + result
            temp //= 10
        
        # Add negative sign if needed
        if is_negative:
            result = "-" + result
        
        return result


# Test the function
print("TASK 2: Number to String Conversion")

print("Testing with integers:")
test_integers = [0, 42, 123, -456, 9999]
for num in test_integers:
    converted = number_to_string(num)
    print(f"  {num:>6} -> '{converted}' (type: {type(converted).__name__})")

print("\nTesting with floats:")
test_floats = [3.14, 2.71828, -9.87, 0.5, 123.456]
for num in test_floats:
    converted = number_to_string(num)
    print(f"  {num:>8} -> '{converted}' (type: {type(converted).__name__})")

print("\nComparison with built-in str():")
test_values = [42, -123, 3.14, -2.71]
for num in test_values:
    custom = number_to_string(num)
    builtin = str(num)
    match = "✓" if custom == builtin else "✗"
    print(f"  {num:>7}: custom='{custom}', built-in='{builtin}' {match}")

# Interactive testing
print("Interactive Testing:")

while True:
    try:
        user_input = input("\nEnter a number (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        num = float(user_input) if '.' in user_input else int(user_input)
        result = number_to_string(num)
        print(f"Number: {num}")
        print(f"Converted: '{result}'")
        print(f"Using str(): '{str(num)}'")
        print(f"Match: {result == str(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
