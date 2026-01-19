import math


def solve_quadratic(a, b, c):
    
    result = {}
    
    # Check if it's actually a quadratic equation
    if a == 0:
        if b == 0:
            if c == 0:
                result['type'] = 'infinite'
                result['message'] = 'Equation 0 = 0 is satisfied for all x'
            else:
                result['type'] = 'no_solution'
                result['message'] = f'Equation {c} = 0 has no solution'
        else:
            # Linear equation: bx + c = 0
            result['type'] = 'linear'
            x = -c / b
            result['solution'] = x
            result['message'] = f'This is a linear equation: bx + c = 0'
    else:
        # Calculate discriminant
        discriminant = b**2 - 4*a*c
        
        result['discriminant'] = discriminant
        
        if discriminant > 0:
            # Two distinct real solutions
            result['type'] = 'two_real'
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            result['x1'] = x1
            result['x2'] = x2
            result['message'] = 'Two distinct real solutions'
            
        elif discriminant == 0:
            # One solution (repeated root)
            result['type'] = 'one_real'
            x = -b / (2*a)
            result['solution'] = x
            result['message'] = 'One solution (repeated root)'
            
        else:
            # Complex solutions
            result['type'] = 'complex'
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            result['x1'] = f"{real_part} + {imaginary_part}i"
            result['x2'] = f"{real_part} - {imaginary_part}i"
            result['message'] = 'Complex conjugate solutions'
    
    return result


def display_solution(a, b, c, result):
    
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    print(f"Type: {result['type']}")
    print(f"Message: {result['message']}")
    
    if 'discriminant' in result:
        print(f"Discriminant (Δ): {result['discriminant']}")
    
    if result['type'] == 'two_real':
        print(f"x₁ = {result['x1']:.6f}")
        print(f"x₂ = {result['x2']:.6f}")
        
        # Verify solutions
        check1 = a * result['x1']**2 + b * result['x1'] + c
        check2 = a * result['x2']**2 + b * result['x2'] + c
        print(f"\nVerification:")
        print(f"  For x₁: a*x₁² + b*x₁ + c = {check1:.10f} (should be ≈ 0)")
        print(f"  For x₂: a*x₂² + b*x₂ + c = {check2:.10f} (should be ≈ 0)")
        
    elif result['type'] == 'one_real':
        print(f"x = {result['solution']:.6f}")
        
        # Verify solution
        check = a * result['solution']**2 + b * result['solution'] + c
        print(f"\nVerification:")
        print(f"  a*x² + b*x + c = {check:.10f} (should be ≈ 0)")
        
    elif result['type'] == 'linear':
        print(f"x = {result['solution']:.6f}")
        
    elif result['type'] == 'complex':
        print(f"x₁ = {result['x1']}")
        print(f"x₂ = {result['x2']}")


# Main program
# Option 1: Predefined test cases
print("TEST CASES:")

test_cases = [
    (1, -5, 6),      # x² - 5x + 6 = 0 → x = 2, 3
    (1, -2, 1),      # x² - 2x + 1 = 0 → x = 1 (double root)
    (1, 0, 1),       # x² + 1 = 0 → complex solutions
    (2, 4, 2),       # 2x² + 4x + 2 = 0 → x = -1 (double root)
    (1, 3, 2),       # x² + 3x + 2 = 0 → x = -1, -2
]

for a, b, c in test_cases:
    result = solve_quadratic(a, b, c)
    display_solution(a, b, c, result)
    print()

# Option 2: User input
print("INTERACTIVE MODE")

while True:
    try:
        print("\nEnter quadratic equation coefficients (or 'quit' to exit):")
        
        a_input = input("Enter coefficient a: ").strip()
        if a_input.lower() == 'quit':
            break
        
        b_input = input("Enter coefficient b: ").strip()
        c_input = input("Enter coefficient c: ").strip()
        
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
        
        result = solve_quadratic(a, b, c)
        display_solution(a, b, c, result)
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"Error: {e}")
