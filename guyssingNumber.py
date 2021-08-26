import random
print("Guessing game")
number=random.randint(1,9)
chances = 0
print("guess the number between 1 to 9")
while chances < 5:
    guess=int(input("Enter The Number"))
    if guess==number:
        print("you WON!!")
        break
    elif guess < number:
        print("number too Low",guess)
    else:
        print("number too High",guess)    
    chances += 1    
if not chances < 5:
    print("you Lose")    


 