#This program is a fast and efficient email spammer
#This is for educational purposes only

#Imports
import smtplib
import prompt

#Main function
def main():
  #Intro statements
  print("Email spammer version 1.0")
  print("This program is for educational purposes only.")
  print("This program will use your gmail account and requires the use of an app password as your password.")
  print("Learn to create an app password here: \nhttps://support.google.com/accounts/answer/185833?hl=en")
  print("When entering your app password, don't include the spaces.")
  
  #User input
  username = input("Enter your gmail address: ")
  password = input("Enter your gmail password: ")
  number = int(input("Enter the number of emails to send: "))
  message = input("Enter the message you would like to send: ")
  toaddress = input("Enter the email address of the recipient: ")
  fromaddress = username

  #Call our login function
  server = login_user(username,password)

  #Call our send mail function
  send_mail(fromaddress,toaddress,message,number,server)

def login_user(username,password):
  server = smtplib.SMTP("smtp.gmail.com:587")
  server.starttls()
  server.login(username,password)
  return server

#This function will send our mail
def send_mail(fromaddress,toaddress,message,number,server):
  for i in range(0,number):
    server.sendmail(fromaddress,toaddress,message)
    print(i+1,"messages sent.")

#Call the main function
main()