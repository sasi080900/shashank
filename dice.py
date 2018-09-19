import random

i=0


while True: 
    x=input("enter 'r' to roll the dice  and 'q' to quit the game")
    if(x=='r'):
        print(random.randint(1,6))
    elif(x=='q'):  
        print("you exit the game")   
        break 
    else:
         print("give either 'r' or 'q' ")    