cache = {} # initializes an empty dictionary named cache, which will be used to store computed values of factorials

def cached_factorial(n): #  defines the cached_factorial function, which calculates the factorial of a given number n 


    # Check if the result is already in the cache
    if n in cache:
        print(f"Fetching from cache for n={n}")
        return cache[n]
    result = 1
    for i in range(1, n + 1):
        result *= i

    cache[n] = result
    print(f"Caching result for n={n}")

    return result

print(cached_factorial(5)) 
print(cached_factorial(6))  