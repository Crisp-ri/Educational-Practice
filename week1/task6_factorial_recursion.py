def factorial_recursive(n):
    # Base cases
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)


def factorial_recursive_with_memoization(n, memo=None):
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = n * factorial_recursive_with_memoization(n - 1, memo)
    return memo[n]


def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def count_recursive_calls(n):
    
    if n <= 0:
        return 1
    
    # Number of calls = 1 (current call) + calls for (n-1)
    return 1 + count_recursive_calls(n - 1)


# Main program

analysis = """
RECURSIVE APPROACH (Without Memoization):

Time Complexity: O(n)
  - We make n function calls: n, n-1, n-2, ..., 1, 0
  - Each function call performs constant time operations (multiplication)
  - Total time = n × O(1) = O(n)

Space Complexity: O(n)
  - Call stack depth is n (recursive calls stack up)
  - Each recursive call uses constant space on the stack
  - Maximum stack depth = n
  - Total space = n × O(1) = O(n)

Recurrence Relation:
  T(n) = T(n-1) + O(1)
  T(0) = O(1)
  
  By solving this recurrence:
  T(n) = T(n-1) + 1
       = T(n-2) + 1 + 1
       = T(n-3) + 1 + 1 + 1
       = ...
       = T(0) + n
       = n + 1
  Therefore, T(n) = O(n)

ITERATIVE APPROACH:

Time Complexity: O(n)
  - Single loop from 2 to n
  - Each iteration performs constant work
  - Total iterations = n-1 ≈ n

Space Complexity: O(1)
  - Only one variable (result) is used
  - No additional data structures
  - Independent of input size

RECURSIVE WITH MEMOIZATION:

Time Complexity: O(n)
  - First calculation for each number: O(n)
  - Subsequent lookups from memo: O(1)
  - Overall: O(n)

Space Complexity: O(n)
  - Memoization dictionary stores n values
  - Call stack depth is still n
  - Total: O(n)

FACTORIAL GROWTH:
  - 5! = 120
  - 10! = 3,628,800
  - 20! = 2,432,902,008,176,640,000
  - The function grows extremely fast!
"""
print(analysis)

# Test and compare implementations

test_values = [0, 1, 5, 10, 15, 20]

print(f"\n{'n':<5} {'Recursive':<20} {'Iterative':<20} {'Memoization':<20}")
print("-" * 70)

for n in test_values:
    try:
        rec_result = factorial_recursive(n)
        iter_result = factorial_iterative(n)
        memo_result = factorial_recursive_with_memoization(n)
        
        print(f"{n:<5} {rec_result:<20} {iter_result:<20} {memo_result:<20}")
    except Exception as e:
        print(f"{n:<5} Error: {e}")

# Performance comparison
print("\n" + "="*70)
print("PERFORMANCE COMPARISON")
print("="*70)

import time

test_cases = [5, 10, 15, 100, 500, 1000]

print(f"\n{'n':<10} {'Recursive (ms)':<20} {'Iterative (ms)':<20} {'Calls for n':<15}")
print("-" * 70)

for n in test_cases:
    if n <= 1000:  # Recursion limit for Python is typically around 1000
        # Recursive
        start = time.time()
        rec_result = factorial_recursive(n)
        rec_time = (time.time() - start) * 1000
        
        # Iterative
        start = time.time()
        iter_result = factorial_iterative(n)
        iter_time = (time.time() - start) * 1000
        
        # Count calls
        calls = count_recursive_calls(n)
        
        print(f"{n:<10} {rec_time:<20.6f} {iter_time:<20.6f} {calls:<15}")
    else:
        print(f"{n:<10} (Skipped - recursion limit)")

# Recursive call visualization

def visualize_recursion(n, depth=0):
    """Visualize the recursive call tree"""
    indent = "  " * depth
    if n <= 0:
        print(f"{indent}factorial(0) = 1 [Base case]")
        return 1
    else:
        print(f"{indent}factorial({n})")
        print(f"{indent}├─ {n} ×")
        result = n * visualize_recursion(n - 1, depth + 1)
        print(f"{indent}└─ result = {result}")
        return result

print("\nRecursive call tree for factorial(5):")
visualize_recursion(5)

# Interactive mode
print("\n" + "="*70)

while True:
    try:
        user_input = input("\nEnter a number to calculate factorial (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        n = int(user_input)
        
        if n < 0:
            print("Error: Factorial is not defined for negative numbers")
            continue
        
        if n > 50:
            print("Warning: Large factorial! Calculations may take time.")
            confirm = input("Continue? (y/n): ").strip().lower()
            if confirm != 'y':
                continue
        
        # Calculate using all methods
        start = time.time()
        rec_result = factorial_recursive(n)
        rec_time = (time.time() - start) * 1000
        
        start = time.time()
        iter_result = factorial_iterative(n)
        iter_time = (time.time() - start) * 1000
        
        start = time.time()
        memo_result = factorial_recursive_with_memoization(n)
        memo_time = (time.time() - start) * 1000
        
        print(f"\n{n}! = {rec_result}")
        print(f"\nPerformance:")
        print(f"  Recursive:     {rec_time:.6f} ms")
        print(f"  Iterative:     {iter_time:.6f} ms")
        print(f"  With memo:     {memo_time:.6f} ms")
        
        # Show number of digits
        num_digits = len(str(rec_result))
        print(f"\nThe result has {num_digits} digits")
        
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
    except RecursionError:
        print("Error: Maximum recursion depth exceeded. Number is too large.")
    except Exception as e:
        print(f"Error: {e}")
