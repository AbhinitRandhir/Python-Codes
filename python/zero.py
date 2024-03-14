import random
list =[]
for i in range(10):
    list.append(random.randint(0,1))
print(list,)
count=0
max=0
for i in list:
    if(i==0):
        count+=1
    else:
        if(count>max):
            max=count
        count=0
print("largest series of zero's is" ,max)