def max(a,b):
    if(a>b):
        print(a)
    else:
        print(b)

def divisible(n):
    if(n%3==0 and n%5==0):
        print("Three and Five")
    elif(n%3==0):
        print("Three")
    elif(n%5==0):
        print("Five")
    else:
        print(n)

def speed(s):
    points=0
    if(s<70):
        print(Ok)
    elif(s>70):
        points = (s-70)/5
    
    if(points<12):
        print(points)
    else:
        print("License Suspended")

def evenOdd(limit):
    for i in range(limit):
        if(i%2 == 0):
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")
        
def lessThan(s):
    if(s<7):
            
        print(f"{s} is less than 7.....{s+1}")
    else:
        print(f"{s} is greater than 7")

if __name__=="__main__":
    a=int(input("Check Max:"))
    b = int(input())
    max(a,b)
    c=int(input("Divisible:"))
    divisible(c)
    d=int(input("Speed:"))
    speed(d)
    e=int(input("Even Odd:"))
    evenOdd(e)
    f=int(input("Less Than 7:"))
    lessThan(f)