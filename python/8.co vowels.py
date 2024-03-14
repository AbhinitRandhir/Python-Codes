name=input("Enter any name : ")
status=False
for i in name:
    if i in ("aeiouAEIOU"):
        status=True
    if(status==True):
        print("Name contain vowels")
    else:
        print("Name not contain vowels")