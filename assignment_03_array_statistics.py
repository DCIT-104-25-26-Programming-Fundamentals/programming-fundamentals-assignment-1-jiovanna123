
def calculate_sum(numbers):
    """Calculates the sum of numbers without using built-in sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculates the average using the custom sum function."""
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Finds the maximum value without using built-in max()."""
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    """Finds the minimum value without using built-in min()."""
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


def main():
    
    n = int(input("How many numbers? "))

    # Requirement: N must be a positive integer
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    # Collect numbers from the user
    numbers = []
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        # Format integer inputs as ints for clean printing if whole
        if num.is_integer():
            num = int(num)
        numbers.append(num)

    # Calculate statistics using custom functions
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    # Print results formatted according to the expected output
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


# Main execution block
if __name__ == "__main__":
    main()
