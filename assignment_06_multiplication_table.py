
def print_single_table(number):
    """
    PART A: Prints the multiplication table for a given number from 1 to 12.
    """
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def print_tables_up_to_n(n):
    """
    PART B: Prints multiplication tables for numbers 1 up to N.
    """
    for num in range(1, n + 1):
        print_single_table(num)
        if num < n:
            print("-" * 27) 


def main():
  
    print("=== PART A: SINGLE TABLE ===")
    user_num = int(input("Enter a number: "))
    
    if user_num <= 0:
        print("Error: Please enter a positive integer.")
    else:
        print_single_table(user_num)

    print("\n" + "=" * 40 + "\n")

    
    print("=== PART B: TABLES FROM 1 TO N ===")
    n = int(input("Enter a number N: "))

    
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)



if __name__ == "__main__":
    main()
