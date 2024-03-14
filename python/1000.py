# lower = int(input("Enter lower range limit:"))
# upper = int(input("Enter upper range limit:"))
# for i in range(lower, upper+1):
#    if((i%3==0) & (i%5==0)):
#        print(i)

# n=input("enter a number:")
# f=1
# for i in range(n):
#     f=f*i
#     print("factorial is :",f)


#convert binery to decimal numbers
bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
  decimal = decimal + int(digit) * 2 ** exponent
exponent = exponent - 1
print("The integer value is", decimal)


#Python script to convert decimal number to binary number
decimal = int(input("Enter a decimal integer: "))
if (decimal == 0):
     print(0)
else:
     print("Quotient Remainder Binary")
     bitString = ""
     while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bitString = str(remainder) + bitString
            print("%5d%8d%12s" % (decimal, remainder,bitString))
print("The binary representation is", bitString)