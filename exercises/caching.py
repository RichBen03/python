cache = {}

def cached_factorial(n):
    # Check if the result is already in the cache
    if n in cache:
        print(f"Fetching from cache for n={n}")
        return cache[n]