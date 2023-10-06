# How to send multiple emails using python. 

import smtplib as s 
ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login('gautam348@gmail.com','jkgsd873')
subject = "test python"
body = "I Love Python!!"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['gautamsonam011@gmail.com']
ob.sendmail('gautam348@gmail.com',listadd,message)
print("send mail")
ob.quit()