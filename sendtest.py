import pywhatkit
import os
import time

#you must have chrome browser and make it the default browser
#create a list in nums with a string format with the desired phone numbers of your choice e.g nums=["+1234567895","+1234569875"]

nums = []


def sendImage():
    for i in nums:
            #path to image in the quatation mark
            pywhatkit.sendwhats_image(i, "Path\\to\\image")
            time.sleep(9)
            os.system("taskkill /im chrome.exe /f")

def sendText():
    for i in nums:
        #write your message in the quatation mark
        pywhatkit.sendwhatmsg_instantly(i, "your massage here", 10, tab_close=True)
        time.sleep(9)
        os.system("taskkill /im chrome.exe /f")



task = int(input("choose a service:\n1-send meassge\n2-send a photo\n"))

if task == 1:
    sendText()
if task == 2:
    sendImage()

 
