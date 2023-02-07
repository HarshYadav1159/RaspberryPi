def remove6(a):
    print(f"Output: {a[6:]}")

def replace(b):
    print(f"Output: {b[:8]} Electronics")

def reverse(a):
    print(f"Reversed String: {a[::-1]}")
    

if __name__=="__main__":
    a=input()
    remove6(a)

    b=input()
    replace(b)
    reverse(a)