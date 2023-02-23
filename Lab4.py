# Ques1. TO sort a dictionary by value
import random
import operator

# RA2011003010746
dic={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2=dict(sorted(dic.items(),key= lambda x:x[1]))
sorted_d = dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
print("Sorted according to ascending values:")
print(dic2)
print("Sorted according to descending values:")
print(sorted_d)
print()

# Ques2. 
aug={}
print("August Tempratures:")
for i in range(1, 11):
    a = random.randint(30,101)
    aug.__setitem__(f"aug{i}", a)
print(aug)
print()
print()

# Ques3.
c30=0
c40=0
for keys in aug:
    if aug[keys] ==30:
        c30+=1
    elif aug[keys]==40:
        c40+=1
    
print(f"Count of 30: {c30}")
print(f"Count of 40: {c40}")

print()
print()
print()

#Ques4.
july={}
for i in range(1, 11):
    a = random.randint(30,101)
    july.__setitem__(f"july{i}", a)
concat= aug
a=concat.update(july)
print("July_August_Temprature_Table:")
print(concat)
print()
print()
print()

#Ques5.
mul=1
sum=0
for keys in concat:
    mul=mul*aug[keys]
    sum=sum+aug[keys] 
l = len(concat)
print(f"Multiplication value is: {mul}")
print(f"Average is: {sum/l}")


