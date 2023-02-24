
dic={}
for i in range(3):
    a=input(" Enter Product Name:")
    b=int(input(" Enter Price: "))
    dic.__setitem__(a,b)

print(dic)

dic2={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
print(f"Maximum: {dic2[max(dic2, key=dic2.get)]}")
print(f"Minimum: {dic2[min(dic2, key=dic2.get)]}")

