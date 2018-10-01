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