def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        print("hi")
        i += 1

# Using the generator function
counter = count_up_to(5)

# Iterating over the generated values
print(next(counter))  # Output: 0
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5

# StopIteration exception will be raised since all values have been generated
#
print(next(counter))  # Raises StopIteration
