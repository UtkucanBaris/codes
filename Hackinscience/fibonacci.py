def fibonacci(n):
    f = [1, 1]
    i = 2
    while i<n:
        f.append(f[-1] + f[-2])
        i += 1
    return f[:n]
print(fibonacci(20))