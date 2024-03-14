def first_diff (str1,str2):
    if str1 == str2:
        return -1
    else:
        return str1.find(str2)
str1=input("Enter string 1:")
str2=input("Enter string 2:")
    #   for i in s1:
    #     for j in s2:
    #        if s1.index(i)==s2.index(j):
    #         if i!=j:
    #           ind=s1.index(i)
    #           return (ind+1
print(first_diff (str1,str2))