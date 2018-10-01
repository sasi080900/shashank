#easy game 
import random 

p={1:'r',2:'p',3:'s'}

while True:
	yc=input("your choise:r/p/s: ")
	cc=p[random.randint(1,3)]

	print("computer gave :" ,cc)