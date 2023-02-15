# Ques.1
list = [2,34,5,6,7,8,9,10]
print(list[::-1])
even=[]
odd=[]

for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])

print(f"Even numbers are: {even}")
print(f"Odd numbers are: {odd}")

# Ques.2
mul=1
for i in range(len(list)):
    mul = mul*list[i]
print(f"Multiplication of list gives: {mul}")