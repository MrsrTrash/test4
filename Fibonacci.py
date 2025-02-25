
def fib(n):
    a = 0
    b = 1
    if n >= 1:
        for i in range(1, n):
            if a < b:
                a += b
            elif b < a:
                b += a
            else:
                b += a
    elif n == 0:
        a = b = 0
    else:
        print("ERROR! Could not calculate nth terms before the 0th term.")
    AB = [a, b]
    n = max(AB)
    return n

n = eval(input("\nPlease enter the nth term you would like from the Fibonacci sequence: "))
print(f"\nThe {n}th term of the Fibonacci sequence is:\n{fib(n)}")


