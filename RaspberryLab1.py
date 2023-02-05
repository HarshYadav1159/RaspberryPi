def arithematic(a,b):
    print(f"Multiply: {a*b}")
    print(f"Additon: {a+b}")
    print(f"Subtract: {a-b}")
    print(f"Division: {a/b}")

def areaOfTriangle(s,a,b,c):
    z = s*(s-a)*(s-b)*(s-c)
    print(f"Area: {z**(0.5)}")



    

if __name__ == "__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    arithematic(a,b)
    s = (a+b+c)/2
    areaOfTriangle(s,a,b,c)

