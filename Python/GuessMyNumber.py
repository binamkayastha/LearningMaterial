import random
import math
#import this #A poem about python

print("""This is
Pi: """ + str(math.pi))
print("This is math.ceil(math.pi) " + str(math.ceil(math.pi)))
print("This is math.floor(math.pi) " + str(math.floor(math.pi)))

player_name = input("What's your name? ")
player_name = player_name.rstrip()
print("Hi " + player_name + " How are you?");

luck = random.randrange(0, 2) #Random number from 0-1
if(luck == 0):
    computer_number = math.pi
else:
    computer_number = random.randrange(0, 101)

print(computer_number)
guessed = False;

while not guessed: #while guessed is equal to false
    inputValid = False
    while not inputValid:
        answer = input("Guess a number from 0, 100: ")
        numanswer = int(answer)
        if(numanswer, int):
            inputValid = True
        else:
            print("Wrong input, try again")
    
    if int(answer) > computer_number:
        print("Number too high");
    elif int(answer) < computer_number:
        print("Number too low");
    elif int(answer) == computer_number:
        guessed = True
        print("You're right");
    else:
        print("Something is wrong, try again");
