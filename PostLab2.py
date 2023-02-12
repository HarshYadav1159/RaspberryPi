def limit(l):
    for i in range(1,l+1):
        print(i)


def factorial(n):
    mul=1
    for i in range(1,n+1):
        mul = mul*i
    print(mul)

if __name__ == '__main__':
    print("Nuber between limit:")
    limit(4)
    print("Factorial of 5:")
    factorial(5)