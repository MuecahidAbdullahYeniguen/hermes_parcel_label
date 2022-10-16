from selenium import webdriver
from selenium.webdriver.common.by import By
import time

MAX_COUNT_FIELDS = 8

#Fields of hermes, their ids and names
userInputEntering = [list(),list()]
userInputReading = list()
userInput = [list(),list()]


fields = ["firstname","lastname","street","houseNumber","zipCode","city","email","phone"]
communicators = ["receiver","sender"]
packageSizes = ["HP","S","M","L","XL","XXL"]
receiverData = ["receiverAddressFirstname","receiverAddressLastname","receiverAddressStreet","receiverAddressHouseNumber","receiverAddressZipCode","receiverAddressCity","receiverEmail","receiverPhone"]
senderData = ["senderAddressFirstname","senderAddressLastname","senderAddressStreet","senderAddressHouseNumber","senderAddressZipCode","senderAddressCity","senderEmail","senderPhone"]
EOF="-"

elementsPackageSize=list()
elementsReceiverData=list()
elementsSenderData=list()
elementsCommunicator=[elementsReceiverData,elementsSenderData]

#Read input of user for parcel labe
filepath = r'C:\Users\MJ\Desktop\python_automation\input.txt'
fp = open(filepath,"r")

lineContents = fp.readline().split(" ")
while EOF not in lineContents[0]:
    for i in range(0,len(lineContents)):
        lineContents[i]= lineContents[i].strip().replace("\n","")
        if lineContents[i]:
            userInputReading.append(lineContents[i])
    lineContents = fp.readline().split(" ")

parcelSize = userInputReading.pop(0)
userInputReading.pop(0)
print(userInputReading)

for j in range(0,len(userInputReading)):
    if j < int(len(userInputReading)/2):
        userInput[0].append(userInputReading[(j)])
    else:
        userInput[1].append(userInputReading[(j)])
print(userInput)
###############################AUTOMATION##########################################################
urlHermes = "https://www.myhermes.de/versenden/paketschein-erstellen/"
#Use browser Chrome
browser = webdriver.Chrome()
browser.get(urlHermes)
#Load pop up dialog
time.sleep(1)
btnCookiesDenie = browser.find_element(By.ID,"uc-btn-deny-banner")
btnCookiesDenie.click()
#Get elements of hermes fields
for size in packageSizes:
    elementsPackageSize.append(browser.find_element(By.ID,"parcelclass-"+size))
for receiverInfo in receiverData:
    elementsReceiverData.append(browser.find_element(By.ID,receiverInfo))
for senderInfo in senderData:
    elementsSenderData.append(browser.find_element(By.ID,senderInfo))


#Enter user input to its field
for i in range(0,len(packageSizes)):
    if packageSizes[i] == parcelSize.upper():
        elementsPackageSize[i].click()

for i in range(0,len(communicators)):
    for j in range(0,MAX_COUNT_FIELDS):
        elementsCommunicator[i][j].send_keys(userInput[i][j])

#Fixed pay by cash
btnPayCash = browser.find_element(By.ID,"payment-cash")
btnPayCash.click()

btnSubmitOrder = browser.find_element(By.ID,"orderSubmitButton")
btnSubmitOrder.click()

#Load download site
time.sleep(2)
#Download parcel label
btnDownload = browser.find_element(By.XPATH,"/html/body/div[3]/section/div/div/div[1]/div/div/div/div[3]/p/span/a[2]")
downloadLink = btnDownload.get_attribute("href")
browser.get(downloadLink)
time.sleep(3)

browser.close()
 

 
 
 
 