s1=input("enter String1 ")
s2=input("enter String2 ") 
if len(s1)!=len(s2):
    print("Length Of Two Strings Are Not Equal!Try Later")
    exit(0)
else:
    r=''
    for i in range(len(s1)):
       r=r+s2[i]+s1[i]
    print(r)