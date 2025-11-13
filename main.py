# Returns the n-th Fibonacci number
def fib(n):
    if n <= 0: return 0
    if n == 1: return 1

    i, j = 0, 1

    while n >= 2:
        i, j = j, i + j
        n -= 1
    
    return j

if __name__ == "__main__":
    n = int(input("Número de Fibonacci desejado:\n> "))
    print(fib(n))