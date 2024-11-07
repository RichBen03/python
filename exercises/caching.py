cache = {} # initializes an empty dictionary named cache, which will be used to store computed values of factorials

def cached_factorial(n): #  defines the cached_factorial function, which calculates the factorial of a given number n 

    if n in cache: # checks whether n is already in the cache
        print(f"Fetching from cache for n={n}") # This line logs that the function is retrieving a cached result, making it clear in the output when the cache is being used.
        return cache[n]
    
    result = 1
    for i in range(1, n + 1):
        result *= i

    cache[n] = result
    print(f"Caching result for n={n}")

    return result

print(cached_factorial(5)) 
print(cached_factorial(6))  