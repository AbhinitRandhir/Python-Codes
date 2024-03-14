def number_of_factors(num):
       factors=[i for i in range(1,num+1) if num%i==0]
       return len(factors)
num=int(input("Enter an integer: "))
print(number_of_factors(num))