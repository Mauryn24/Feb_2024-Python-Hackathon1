def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence
    if n <= 0:
        return fibonacci_sequence  # Return an empty list if n is non-positive
    elif n == 1:
        fibonacci_sequence.append(0)  # Return [0] if n is 1
    else:
        fibonacci_sequence.extend([0, 1])  # Start the sequence with [0, 1]
        a, b = 0, 1  # Initialize variables for the first two terms
        for _ in range(2, n):  # Loop from the 3rd term to the nth term
            c = a + b  # Calculate the next term
            fibonacci_sequence.append(c)  # Add the next term to the sequence
            a, b = b, c  # Update variables for the next iteration
    return fibonacci_sequence  # Return the generated Fibonacci sequence


# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("The Fibonacci sequence up to", num_terms, "terms is:", fibonacci_sequence)
