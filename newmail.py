import smtplib
import getpass

myemail="sasi080900@gmail.com"
recemail="laughinggidoll2000@gmail.com"
password=input("your password please:" )
#creates SMPT session 
s=smtplib.SMTP('smtp.gmail.com',587) 


# start TLS for security  
s.starttls()

#authentication 
s.login(myemail,password)

#message to be send 
message ="hello gevisha "

#sending  the mail 
s.sendmail("sasi080900@gmail.com","laughinggidoll2000@gmail.com",message)
s.quit()