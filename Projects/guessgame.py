secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit :
    guess= int(input('Guess: '))
    guess_count+=1
    if guess == secret_number :
        print(" You Won!")
        break
else:
    print("Sorry !, You Failed")


secret_number=5
i=0
guess_limit=3
while i < guess_limit : 
    guess=int(input('Guess: '))
    i+=1
    if guess == secret_number:
        print("you won!")
        break
else:
    print("Sorry !, You Failed")
