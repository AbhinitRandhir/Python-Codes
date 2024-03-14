import random
r=[]
for i in range(20): 
    r.append(random.randint(1,100))
# (a) Print the list.
print("The list with 20 random numbers is:",r)
# (b) Print the average of the elements in the list.
print("The Average of list with 20 random numbers is:",round(sum(r)/len(r),2))
# (c) Print the largest and smallest values in the list.
print("Maximun Element is:",max(r))
print("Minimum Element is:",min(r))
#(d) Print the second largest and second smallest entries in the list
r1=list(set(r))
r1.sort()
print("Second largest element is:",r1[-2])
print("Second smallest element is:",r1[1])
#(e) Print how many even numbers are in the list.
even=[i for i in r if i%2==0]
print("even numbers count in the list is:",len(even))