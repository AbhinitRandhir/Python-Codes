# sen=input()
# #def swap(sen):
# s=sen.swapcase()
# s1=s.split()
# l=len(s1)

# for i in range(l):
#     print(s1[l-1-i],end=" ")
def swap(sen):
    s=sen.swapcase()
    s1=s.split()
    for i in range(len(s1)):
     print(s1[len(s1)-1-i],end=" ")
sen=input()
swap(sen)