def circle(r):
    print(f"Area:{3.14*(r**2)}")

def output(s1,s2):
    print("Output: " +s1+s2)

if __name__=="__main__":
    r = int(input())
    circle(r)
    s1 = input()
    s2 = input()
    output(s1,s2)
