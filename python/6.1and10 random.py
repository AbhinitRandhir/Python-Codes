import random
num=random.randint(1,10)
while True:
    guess=int(input("Guess a number "))
    if(guess==num):
       print('guessed')
       break
    else:
       print("Sorry try again")