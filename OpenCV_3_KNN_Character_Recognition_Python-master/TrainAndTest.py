# TrainAndTest.py

import cv2
import numpy as np
import operator
import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
######
from reportlab.pdfgen import canvas
import datetime
#from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import smtplib
import random

# module level variables ##########################################################################
MIN_CONTOUR_AREA = 70

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

###################################################################################################
class ContourWithData():

    # member variables ############################################################################
    npaContour = None           # contour
    boundingRect = None         # bounding rect for contour
    intRectX = 0                # bounding rect top left corner x location
    intRectY = 0                # bounding rect top left corner y location
    intRectWidth = 0            # bounding rect width
    intRectHeight = 0           # bounding rect height
    fltArea = 0.0               # area of contour

    def calculateRectTopLeftPointAndWidthAndHeight(self):               # calculate bounding rect info
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):                            # this is oversimplified, for a production grade program
        if self.fltArea < MIN_CONTOUR_AREA: return False        # much better validity checking would be necessary
        return True

###################################################################################################
def main():
    allContoursWithData = []                # declare empty lists,
    validContoursWithData = []              # we will fill these shortly

    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)                  # read in training classifications
    except:
        print( "error, unable to open classifications.txt, exiting program\n")
        os.system("pause")
        return
    # end try

    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)                 # read in training images
    except:
        print( "error, unable to open flattened_images.txt, exiting program\n")
        os.system("pause")
        return
    # end try

    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))       # reshape numpy array to 1d, necessary to pass to call to train

    kNearest = cv2.ml.KNearest_create()                   # instantiate KNN object

    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    imgTestingNumbers = cv2.imread("img{}.png".format(i))          # read in testing numbers image

    if imgTestingNumbers is None:                           # if image was not read successfully
        print ("error: image not read from file \n\n")        # print error message to std out
        os.system("pause")                                  # pause so user can see error message
        return                                              # and exit function (which exits program)
    # end if

    imgGray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)       # get grayscale image
    imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                    # blur

                                                        # filter image from grayscale to black and white
    imgThresh = cv2.adaptiveThreshold(imgBlurred,                           # input image
                                      255,                                  # make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # use gaussian rather than mean, seems to give better results
                                      cv2.THRESH_BINARY_INV,                # invert so foreground will be white, background will be black
                                      11,                                   # size of a pixel neighborhood used to calculate threshold value
                                      2)                                    # constant subtracted from the mean or weighted mean

    imgThreshCopy = imgThresh.copy()        # make a copy of the thresh image, this in necessary b/c findContours modifies the image

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,             # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                                 cv2.RETR_EXTERNAL,         # retrieve the outermost contours only
                                                 cv2.CHAIN_APPROX_SIMPLE)   # compress horizontal, vertical, and diagonal segments and leave only their end points

    for npaContour in npaContours:                             # for each contour
        contourWithData = ContourWithData()                                             # instantiate a contour with data object
        contourWithData.npaContour = npaContour                                         # assign contour to contour with data
        contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)     # get the bounding rect
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()                    # get bounding rect info
        contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)           # calculate the contour area
        allContoursWithData.append(contourWithData)                                     # add contour with data object to list of all contours with data
    # end for

    for contourWithData in allContoursWithData:                 # for all contours
        if contourWithData.checkIfContourIsValid():             # check if valid
            validContoursWithData.append(contourWithData)       # if so, append to valid contour list
        # end if
    # end for

    validContoursWithData.sort(key = operator.attrgetter("intRectX"))         # sort contours from left to right

    strFinalString = ""         # declare final string, this will have the final number sequence by the end of the program

    for contourWithData in validContoursWithData:            # for each contour
                                                # draw a green rect around the current char
        cv2.rectangle(imgTestingNumbers,                                        # draw rectangle on original testing image
                      (contourWithData.intRectX, contourWithData.intRectY),     # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth, contourWithData.intRectY + contourWithData.intRectHeight),      # lower right corner
                      (0, 255, 0),              # green
                      2)                        # thickness

        imgROI = imgThresh[contourWithData.intRectY : contourWithData.intRectY + contourWithData.intRectHeight,     # crop char out of threshold image
                           contourWithData.intRectX : contourWithData.intRectX + contourWithData.intRectWidth]

        imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))             # resize image, this will be more consistent for recognition and storage

        npaROIResized = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))      # flatten image into 1d numpy array

        npaROIResized = np.float32(npaROIResized)       # convert from 1d numpy array of ints to 1d numpy array of floats

        retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 1)     # call KNN function find_nearest

        strCurrentChar = str(chr(int(npaResults[0][0])))                                             # get character from results

        strFinalString = strFinalString + strCurrentChar            # append current char to full string
    # end for

        r= strFinalString
    ###########################################
    iisf=sqlite3.connect("chalan.db")
    cur=iisf.cursor()
        
    sql="select * from vehicle where vehicle_number='"+r+"';"
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
                    ##
                message.attach(MIMEText(body,'plain'))
                filename="{}.pdf".format(y[1])
                attachment=open(filename,'rb')
                part=MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('content-Disposition','attachment; filename=' +filename)
                message.attach(part)
                text=message.as_string()
                    ##
                    ##
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login(mail,password)
                    ##
                    

                server.sendmail(mail,person,text)
                server.quit()
                print("Chalan send on number {}".format(r))

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
                print("{} vehicle registration cancel".format(r))

        except:
            print("{} VEHICLE NOT REGISTERED".format(r))
#########################3

    
    
    cv2.imshow("imgTestingNumbers", imgTestingNumbers)
    # show input image with green boxes drawn around found digits
    cv2.waitKey(2)
    

    #cv2.destroyAllWindows()             # remove windows from memory

    return

###################################################################################################
for i in range(1,5):
    try:
        if __name__ == "__main__":
            main()
            i=i+1
    except:
        print("none")
# end if









