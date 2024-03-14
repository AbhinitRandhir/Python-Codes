# Data Number type

# str1="MONU"
# str2="Kumar"
# str3=str1+str2
# print("%d",str3)

# a=10
# print(type(a))
# b=2.34
# print(type(b))
# c=10+3j
# print(type(c))

# Data boolean type

# status=True
# print(status)

# status=False
# print(status)

# Data type string
# s='Aditya'
# print(type(s))

# s="Aditya"
# print(type(s))

# s="'Aditya'"
# print(type(s))

# LIst Data types
# l=[1,23,34,45,67]
# print(type(l))

# l=[1,23,"monu",34.87]
# print(type(l))

# n = int(input ("Enter the number you want to print: "))     
# # Take input from user that how many numbers you want to print  
# a = 0    
# b = 1    
# for i in range(0,n):  
#     print(a, end = " ")             # a:0;    a:1;       a:2  
#     c = a+b                     #c=0+1=1; c= 1+1=2;  c=1+2=3  
#     a = b               #a=1    ; a=1;       a=2  
#     b = c               #b=1    ; b=2;       b=3  

# lower = int(input("Enter lower range limit:"))
# upper = int(input("Enter upper range limit:"))
# for i in range(lower, upper+1):
#    if((i%4==0) & (i%6==0)):
#       print(i)

# sub1=int(input("Enter marks of the first subject: "))
# sub2=int(input("Enter marks of the second subject: "))
# sub3=int(input("Enter marks of the third subject: "))
# sub4=int(input("Enter marks of the fourth subject: "))
# sub5=int(input("Enter marks of the fifth subject: "))
# avg=(sub1+sub2+sub3+sub4+sub4)/5
# if(avg>=90):
#     print("Grade: A")
# elif(avg>=80&avg<90):
#     print("Grade: B")
# elif(avg>=70&avg<80):
#     print("Grade: C")
# elif(avg>=60&avg<=70):
#     print("Grade: D")
# else:
#     print("Grade: F")

class ABC:
        a=10
obj=ABC()
print(obj.a)

