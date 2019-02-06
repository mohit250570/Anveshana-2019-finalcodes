
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import sqlite3
import smtplib
import random
import datetime
from reportlab.pdfgen import canvas
from twilio.rest import Client
###############
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 400)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(220, 159, 65, 193), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 20, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.symbol = QtWidgets.QLabel(self.centralwidget)
        self.symbol.setGeometry(QtCore.QRect(0, 70, 221, 221))
        self.symbol.setText("")
        self.symbol.setPixmap(QtGui.QPixmap("download.jpg"))
        self.symbol.setObjectName("symbol")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 111, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 250, 111, 41))
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "          E-CHALAN GENERATOR"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "    VEHICLE NUMBER"))
        self.pushButton.setText(_translate("MainWindow", "GENERATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))

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
                cut=y[4]
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
# Your Account SID from twilio.com/console
                    account_sid = "ACd2b674f69ac2c32de823fc62bb3fd7ee"
# Your Auth Token from twilio.com/console
                    auth_token  = "94d7f58e49c9df36a510c6583e350c10"
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                    to="+91{}".format(y[4]), 
                    from_="+18155696078",
                    body="Hello {} vehicle number {} model {} producing excesive amount of harmfull gases. \n please submit fine of Rs 1000 to the nearest RTO office or police station \n along with e-chalan copy that send to your gmail.. \n Thank You \n RTO office  ".format(y[1],y[0],y[3]))

                    print(message.sid)

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
                    # Your Account SID from twilio.com/console
                    account_sid = "ACd2b674f69ac2c32de823fc62bb3fd7ee"
# Your Auth Token from twilio.com/console
                    auth_token  = "94d7f58e49c9df36a510c6583e350c10"
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                    to="+91{}".format(y[4]), 
                    from_="+18155696078",
                    body="Hello {} vehicle number {} model {} is older then 15 years so we are cancelling your vehicle registration.\n Thank You \n RTO office  ".format(y[1],y[0],y[3]))

                    print(message.sid)


                    server.quit()
                    print("CHALAN SEND")

            except:
                print("VEHICLE NOT REGISTERED")
#########################3

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

