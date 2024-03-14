import random
l=[]
for i in range(20):
   l.append(random.randint(0,1))
print(l)
count=0
max=0
for i in range (len(l)):
    if(l[i]==0):
        count+=1
    if(l[i]!=0) or i==len(l)-1:
        if(max<count):
            max=count
        count=0
print(max)