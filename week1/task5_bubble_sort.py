def bubble_sort(arr):
    n = len(arr)
    arr_copy = arr.copy()  # Don't modify original array
    
    comparisons = 0
    swaps = 0
    iterations = 0
    
    # Bubble sort algorithm
    for i in range(n):
        iterations += 1
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            comparisons += 1
            
            # Swap if the element is greater than the next element
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swaps += 1
                swapped = True
        
        # If no swaps were made, array is already sorted
        if not swapped:
            break
    
    return arr_copy, comparisons, swaps, iterations


def get_array_from_user():
    
    print("\nEnter array elements in one of the following ways:")
    print("1. Space-separated numbers: 5 3 8 1 9")
    print("2. Or enter 'random' for a random array: random 10 (generates 10 random numbers)")
    
    user_input = input("\nEnter array elements: ").strip()
    
    if user_input.lower() == 'q':
        return None
    
    if user_input.lower().startswith('random'):
        import random
        parts = user_input.split()
        if len(parts) > 1:
            try:
                size = int(parts[1])
                arr = [random.randint(1, 100) for _ in range(size)]
                print(f"Generated random array of size {size}")
                return arr
            except ValueError:
                print("Error: Please provide valid number for array size")
                return None
        else:
            print("Usage: random <size>")
            return None
    
    try:
        arr = [float(num.strip()) for num in user_input.split() if num.strip()]
        
        # Convert to int if all are integers
        if all(num == int(num) for num in arr):
            arr = [int(num) for num in arr]
        
        return arr
    except ValueError:
        print("Error: Invalid input. Please enter numbers separated by spaces.")
        return None


def display_sorting_steps(arr):
    """Display step-by-step sorting process"""
    
    n = len(arr)
    arr_copy = arr.copy()
    
    print("\nStep-by-step sorting process:")
    print(f"Original array: {arr_copy}")
    print("-" * 60)
    
    step = 0
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                step += 1
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                print(f"Step {step}: Swapped {arr_copy[j + 1]} and {arr_copy[j]} -> {arr_copy}")
                swapped = True
        
        if not swapped:
            print(f"Pass {i + 1}: No swaps needed, array is sorted")
            break
        else:
            print(f"End of pass {i + 1}: {arr_copy}")
            print()
    
    return arr_copy


# Main program
print("\nBubble sort is a simple sorting algorithm that repeatedly steps through")
print("the list, compares adjacent elements, and swaps them if they are in the")
print("wrong order. The algorithm gets its name because smaller elements 'bubble'")
print("to the top of the list.")

# Test cases
print("TEST CASES")

test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9],
    [1],
    [3, 3, 3],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]

for arr in test_arrays:
    print(f"\nOriginal array: {arr}")
    sorted_arr, comparisons, swaps, iterations = bubble_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    print(f"Statistics:")
    print(f"  Comparisons: {comparisons}")
    print(f"  Swaps: {swaps}")
    print(f"  Iterations (passes): {iterations}")
    print(f"  Array size: {len(arr)}")

# Interactive mode
print("\n" + "="*70)
print("INTERACTIVE MODE")
print("="*70)

while True:
    print("\n" + "-"*70)
    print("Menu:")
    print("  1. Sort array with details")
    print("  2. Show step-by-step sorting process")
    print("  3. Performance comparison on different sizes")
    print("  4. Quit")
    
    choice = input("\nChoose option (1-4): ").strip()
    
    if choice == '4':
        break
    elif choice == '1':
        arr = get_array_from_user()
        if arr is not None:
            print(f"\nOriginal array: {arr}")
            sorted_arr, comparisons, swaps, iterations = bubble_sort(arr)
            print(f"Sorted array:   {sorted_arr}")
            print(f"\nStatistics:")
            print(f"  Array size: {len(arr)}")
            print(f"  Comparisons: {comparisons}")
            print(f"  Swaps: {swaps}")
            print(f"  Iterations (passes): {iterations}")
    
    elif choice == '2':
        arr = get_array_from_user()
        if arr is not None:
            display_sorting_steps(arr)
    
    elif choice == '3':
        import random
        print("\nPerformance comparison on different array sizes:")
        print("-" * 70)
        print(f"{'Size':<10} {'Comparisons':<15} {'Swaps':<15} {'Time':<15}")
        print("-" * 70)
        
        import time
        sizes = [10, 50, 100, 500]
        for size in sizes:
            arr = [random.randint(1, 1000) for _ in range(size)]
            
            start_time = time.time()
            sorted_arr, comparisons, swaps, iterations = bubble_sort(arr)
            end_time = time.time()
            
            elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            print(f"{size:<10} {comparisons:<15} {swaps:<15} {elapsed_time:<15.4f} ms")
    
    else:
        print("Invalid choice. Please try again.")