#lets start a game 
import random 


count=0 
def roll(): 
	return random.randint(1,6 )

while(count<=100):
	n=input("press r to roll the dice and q to quit the game ")
	if(n=='r'):
		r = roll()
		count=count+r
		print("u got " ,r )  
		print("new position is ",count )


		if(count==8):
		   count=37
		   print("you got a ladder u r current position is",count)
		elif(count==13): 
		     count=34
		     print("you got a ladder u r current position is",count) 
		elif (count==25):    
		      count=4 
		      print("you had bitten by snake & u r current is ",count)
		elif(count==40):   
		     count=68
		     print("you git a ladder u r current position is",count) 
		elif(count==52):  
		     count=81
		     print("you git a ladder u r current position is",count)
		elif(count==65):    
		     count=46
		     print("you had bitten by snake & u r current is ",count)
		elif(count==76):  
		     count=97
		     print("you git a ladder u r current position is",count)
		elif(count==89):   
		    count=70
		    print("you had bitten by snake & u r current is ",count)
		elif(count==93):    
		     count=74
		     print("you had bitten by snake & u r current is ",count)
		elif(count==100):
			print("you won the game ")
			break 
		if(count+r>100):
		   count=count-r 
		   print("you can't go forward throw the dice again////")   
			OUTPUT
	press r to roll the dice and q to quit the game r
u got  3
new position is  3
press r to roll the dice and q to quit the game r
u got  3
new position is  6
press r to roll the dice and q to quit the game r
u got  1
new position is  7
press r to roll the dice and q to quit the game r
u got  3
new position is  10
press r to roll the dice and q to quit the game r
u got  6
new position is  16
press r to roll the dice and q to quit the game r
u got  6
new position is  22
press r to roll the dice and q to quit the game r
u got  1
new position is  23
press r to roll the dice and q to quit the game 
press r to roll the dice and q to quit the game r
u got  5
new position is  28
press r to roll the dice and q to quit the game r
u got  5
new position is  33
press r to roll the dice and q to quit the game r
u got  5
new position is  38
press r to roll the dice and q to quit the game r
u got  4
new position is  42
press r to roll the dice and q to quit the game r
u got  5
new position is  47
press r to roll the dice and q to quit the game r
u got  1
new position is  48
press r to roll the dice and q to quit the game r
u got  4
new position is  52
you git a ladder u r current position is 81
press r to roll the dice and q to quit the game r
u got  5
new position is  86
press r to roll the dice and q to quit the game r
u got  5
new position is  91
press r to roll the dice and q to quit the game r
u got  5
new position is  96
you can't go forward throw the dice again////
press r to roll the dice and q to quit the game r
u got  6
new position is  97
you can't go forward throw the dice again////
press r to roll the dice and q to quit the game r
u got  3
new position is  94
press r to roll the dice and q to quit the game r
u got  3
new position is  97
press r to roll the dice and q to quit the game r
u got  4
new position is  101
you can't go forward throw the dice again////
press r to roll the dice and q to quit the game r
u got  1
new position is  98
press r to roll the dice and q to quit the game r
u got  2
new position is  100
you won the game 
		
