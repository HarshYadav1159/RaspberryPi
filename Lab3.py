# Ques.1(Swap first and last element of a list)
list = [2,3,-4,5,-66,7]
temp =0
temp = list[0]
list[0] =list[5]
list[5]=temp
print(f"Swapped list is: {list}")

# Ques.2
list.sort()
print(f"Smallest N numbers: {list[:3]}") 
print(f"Greatesst N numbers: {list[len(list)-3:]}") 

# Ques.3
sum=0
for i in range(len(list)):
    sum = sum+list[i]
print(f"Sum is: {sum}")

# Ques.4
print("Positive numbers are: ")
for i in range(len(list)):
    if list[i] >= 0:
        print(f" {list[i]} ")
    
# Ques.5
print('First 5 and last 5 numbers are: ')
for i in range(1, 31):
    if i <= 5 or i>25:
        print(f"{i**2}")
