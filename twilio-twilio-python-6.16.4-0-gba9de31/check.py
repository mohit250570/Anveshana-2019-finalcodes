from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import sqlite3
import smtplib
import random
    #################
    def send(self):
        iisf=sqlite3.connect("chalan.db")
        cur=iisf.cursor()
        data=self.lineEdit.text()
        sql="select * from vehicle where vehicle_number='"+data+"';"
        x=cur.execute(sql)

        if x!=None:
            y=cur.fetchone()
            try:
                mail="shreshthar.speed17@gmail.com"
                password="tommymyfriend"
                sub="E-CHALAN VEHICLE POLLUTION"
                person=y[2]
                a=y[5]
                d = datetime.datetime.today()
                date = datetime.datetime.strptime(a, "%Y-%m-%d")
                com=d.year-date.year
                if(com<15):
                    body = "Subject: {}\n Hello {} vehicle number {} model {} producing excesive amount of harmfull gases. \n please submit fine of Rs 1000 to the nearest RTO office or police station. \n Thank You \n RTO office".format(sub,y[1],y[0],y[3])        
                    c= canvas.Canvas("{}.pdf".format(y[1]))
                    c.drawString(280,800 ,"E-challan")
                    c.drawString(50,650,"Date:{}".format(datetime.datetime.now()))
                    c.drawString(50,630,"Chalan No. {}".format(random.randint(654789,987654)))
                    seal= 'download.jpg'
                    c.drawImage(seal,260,670,width=100, height=100)
                    c.drawString(50,610,"Sir,")
                    c.drawString(80,590,"{} vehicle number {} model {} ".format(y[1],y[0],y[3]))
                    c.drawString(80,570,"producing excesive amount of harmfull gases.")
                    c.drawString(80,550,"please submit fine of Rs 1000 to the nearest RTO office or police station.")
                    c.drawString(50,500,"Thank You:")
                    c.drawString(50,480,"RTO OFFICE")
                    c.save()
                    subject="E-chalan"
                    message=MIMEMultipart()
                    message['From']=mail
                    message['To']=person
                    message['Subject']=subject
                    message.attach(MIMEText(body,'plain'))
                    filename="{}.pdf".format(y[1])
                    attachment=open(filename,'rb')
                    part=MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('content-Disposition','attachment; filename=' +filename)
                    message.attach(part)
                    text=message.as_string()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login(mail,password)
                    server.sendmail(mail,person,text)
                    server.quit()
                    print("CHALAN SEND")

                else:
                    body = "Subject: {}\n Hello {} vehicle number {} model {} is cross the limit of 15 years so we cancelling your registration number.".format(sub,y[1],y[0],y[3])        
                    c= canvas.Canvas("{}.pdf".format(y[1]))
                    c.drawString(280,800 ,"E-challan")
                    c.drawString(50,650,"Date:{}".format(datetime.datetime.now()))
                    c.drawString(50,630,"Chalan No. {}".format(random.randint(654789,987654)))
                    seal= 'download.jpg'
                    c.drawImage(seal,260,670,width=100, height=100)
                    c.drawString(50,610,"Sir,")
                    c.drawString(80,590,"{} vehicle number {} model {} is cross the limit of 15 year ".format(y[1],y[0],y[3]))
                    #c.drawString(80,570,"is cross the limit of 15 year ")
                    c.drawString(80,570,"So we are cancelling you vehicle registration.")
                    c.drawString(50,530,"Thank You:")
                    c.drawString(50,500,"RTO OFFICE")
                    c.save()
                    subject="Vechicle Registration Cancellation"
                    message=MIMEMultipart()
                    message['From']=mail
                    message['To']=person
                    message['Subject']=subject
                    message.attach(MIMEText(body,'plain'))
                    filename="{}.pdf".format(y[1])
                    attachment=open(filename,'rb')
                    part=MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('content-Disposition','attachment; filename=' +filename)
                    message.attach(part)
                    text=message.as_string()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login(mail,password)
                    server.sendmail(mail,person,text)
                    server.quit()
                    print("CHALAN SEND")

            except:
                print("VEHICLE NOT REGISTERED")
#########################3







from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd2b674f69ac2c32de823fc62bb3fd7ee"
# Your Auth Token from twilio.com/console
auth_token  = "94d7f58e49c9df36a510c6583e350c10"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917557462911", 
    from_="+18155696078",
    body="Hello from Python!")

print(message.sid)
