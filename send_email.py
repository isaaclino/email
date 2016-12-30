import smtplib
import os

def send_email(username, password, email, message):
    
    # smtpOnj represents SMTP mail server and passing the paramater
    print "\n"
    print "opening SMTP protocol..."
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    
    #object ehlo() method is important after calling SMTP
    print "stablishing connection..."
    smtpObj.ehlo()
    
    #stattls method is used to acquire TLS and encrypt your message
    print "acquiring TLS encryption..."
    smtpObj.starttls()
    
    # logging in using username and password from user
    print "logging in..."
    smtpObj.login(username, password)   

    #after acquiring encryption and logging in sendmail() method to send the information 
    print "sending email..."
    smtpObj.sendmail(username, email, message)
    
    #calling quit() method to disconnect the connection
    print "closing connection..."
    smtpObj.quit()


def main():

    os.system('clear')
    print "\n\t -- Send eMail script --\n\n"
    
    print "* Enter SENDER (your) information *\n"
    
    #get the information from the user 
    username = raw_input('Senders email: ') 
    password = raw_input('Senders password: ')

    print "\n* Now enter RECIPIENT  information *\n"
    
    email = raw_input('Recipient email: ')
    message = raw_input('Enter message you want to send: ')

    #call the function and pass user information
    send_email(username, password, email, message)

    print "\n Your email has been successfully sent !\n"

if __name__ == "__main__": main()

#from email.mime.text import MIMEText
#from datetime import date
#import smtplib

#SMTP_SERVER = "smtp.gmail.com"
#SMTP_PORT = 587
#SMTP_USERNAME = "user@gmail.com"
#SMTP_PASSWORD = "xxx" it asks for password instead of hardcoded"

#EMAIL_TO = "to_user@server.com"
#EMAIL_FROM = "from_user@gmail.com"
#EMAIL_SUBJECT = "Demo Email : "

#DATE_FORMAT = "%d/%m/%Y"
#EMAIL_SPACE = ", "

#DATA='This is the content of the email.'

#def send_email():
#    msg = MIMEText(DATA)
#    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
#    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
#    msg['From'] = EMAIL_FROM
#    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#    mail.ehlo()
#    mail.starttls()
#    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
#    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
#    mail.quit()

#if __name__=='__main__':
#    send_email()
