# this is a generic email script
# please substitute the following
# USERNAME -> your gmail account email : myname@gmail.com
# PASSWORD -> your gmail account password  : mypasscode1
# EMAIL -> email you want to send to  : user@hotmail.com

import smtplib


    
    # smtpOnj represents SMTP mail server and passing the paramater
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    
    #object ehlo() method is important after calling SMTP
    smtpObj.ehlo()
    
    #stattls method is used to aquire TLS and encrypt your message
    smtpObj.starttls()
    
    # loggin in using username and password from user
    smtpObj.login('USERNAME', 'PASSWORD')   

    #after aquaring encryption and logging in sendmail() method to send the information 
    smtpObj.sendmail('USERNAME', 'EMAIL', 'This is a test, Hello World!')
    
    #calling quit() method to disconnect the connection
    smtpObj.quit()

