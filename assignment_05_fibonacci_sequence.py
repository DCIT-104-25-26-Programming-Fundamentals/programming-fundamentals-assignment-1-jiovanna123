
def generate_fibonacci(n):
    """
    PART A: Generates and returns a list containing the first N Fibonacci numbers.
    """
    if n <= 0:
        return []

    
    sequence = [0, 1]

    if n == 1:
        return [0]

    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


def is_fibonacci_number(num):
    """
    PART B: Determines whether a given non-negative integer is a Fibonacci number.
    Uses an iterative loop until the sequence reaches or exceeds num.
    """
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


def main():
    print("=== PART A: PRINT FIRST N TERMS ===")
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        fib_list = generate_fibonacci(n)
        
        output_str = " ".join(str(val) for val in fib_list)
        print(f"Fibonacci sequence: {output_str}")

    print("\n" + "=" * 40)
    print("=== PART B: CHECK FIBONACCI NUMBER ===")
    check_num = int(input("Enter a number to check: "))

    if is_fibonacci_number(check_num):
        print(f"{check_num} is a Fibonacci number.")
    else:
        print(f"{check_num} is NOT a Fibonacci number.")



if __name__ == "__main__":
    main()
