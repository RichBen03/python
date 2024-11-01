# Task: Create a prime factorization generator. For any given integer input, use loops to break it down into its prime factors, returning a list of factors. Avoid using external libraries for prime checking.
def prime_factors(n):
    # List to store the prime factors
    factors = []
    
    # Check for the number of 2s that divide n (handle even numbers)
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 upwards
    factor = 3
    while factor * factor <= n:
        # If factor divides n, it's a factor
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2  # Only check odd numbers
    
    # If n is still greater than 2, then n itself is a prime factor
    if n > 2:
        factors.append(n)
    
    return factors

# Test the function
number = int(input("Enter an integer to find its prime factors: "))
print(f"Prime factors of {number}: {prime_factors(number)}")
