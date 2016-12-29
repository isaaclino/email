import smtplib

def send_email(username, password, recepiant_email, message):
    
    # smtpOnj represents SMTP mail server and passing the paramater
    print "calling SMTP server...\n"
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    
    #object ehlo() method is important after calling SMTP
    print "stablishing connection...\n"
    smtpObj.ehlo()
    
    #stattls method is used to aquire TLS and encrypt your message
    print "aquaring TLS encryption...\n"
    smtpObj.starttls()
    
    # loggin in using username and password from user
    print "loggin in...\n"
    smtpObj.login(username, password)   

    #after aquaring encryption and logging in sendmail() method to send the information 
    print "sending email...\n"
    smtpObj.sendmail(username, recepiant_email, message)
    
    #calling quit() method to disconnect the connection
    print "closing connection...\n "
    smtpObj.quit()


def main():

    print "\n\t --Welcome to eMail script --\n\n"
    
    print "* Enter SENDER (your) information *\n"
    
    #get the information from the user 
    username = raw_input('Senders email: ') 
    password = raw_input('Senders password: ')

    print "\n* Now enter RECEPIANT  information *\n"
    
    recepiant_email = raw_input('Recepiant email: ')
    message = raw_input('Enter message you want to send: ')

    #call the function and pass user information
    send_email(username, password, recepiant_email, message)

    print "Your email has been successfully sent !\n"

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
