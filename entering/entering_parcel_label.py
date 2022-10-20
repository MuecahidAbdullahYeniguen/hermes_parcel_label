import email
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

MAX_COUNT_FIELDS = 8

# Fields of hermes, their ids and names
userInputEntering = [list(), list()]
userInputReading = list()
userInput = [list(), list()]

# C:\Users\MJ\AppData\Local\Programs\Python\Python310\python.exe

communicators = ["receiver", "sender"]
packageSizes = ["HP", "S", "M", "L", "XL", "XXL"]
receiverFields = ["receiverAddressFirstname", "receiverAddressLastname", "receiverAddressStreet",
                  "receiverAddressHouseNumber", "receiverAddressZipCode", "receiverAddressCity", "receiverEmail", "receiverPhone"]
senderFields = ["senderAddressFirstname", "senderAddressLastname", "senderAddressStreet",
                "senderAddressHouseNumber", "senderAddressZipCode", "senderAddressCity", "senderEmail", "senderPhone"]
receiverData = dict.fromkeys(receiverFields, "")
senderData = dict.fromkeys(senderFields, "")
data = [receiverData, senderData]
fields = [receiverFields, senderFields]

"""receiverInput = list()
senderInput = list()
input = [receiverInput, senderInput]"""

elementsPackageSize = dict.fromkeys(packageSizes, "")
elementsReceiverData = dict.fromkeys(receiverFields, "")
elementsSenderData = dict.fromkeys(senderFields, "")
elementsCommunicator = [elementsReceiverData, elementsSenderData]


# Get input of user for parcel label

exit = True


while  exit:
    print(exit)
    print("Package: ")
    parcelSize = input("Enter parcel size: ").upper()
    print("\n")
    for i in range(0, len(communicators)):
        print("{} address:".format(communicators[i]))
        for field in fields[i]:
            data[i][field] = input("Enter {}: ".format(field))
        print("\n")
    print(data)

    

    ###############################AUTOMATION##########################################################
    #Get elements of hermes fields
    urlHermes = "https://www.myhermes.de/versenden/paketschein-erstellen/"
    #Use browser Chrome
    browser = webdriver.Chrome()
    browser.get(urlHermes)
    #Load pop up dialog
    time.sleep(1)
    btnCookiesDenie = browser.find_element(By.ID,"uc-btn-deny-banner")
    btnCookiesDenie.click()
    elementsPackageSize[parcelSize]= browser.find_element(By.ID,"parcelclass-"+parcelSize)

    for field in receiverFields:
        elementsReceiverData[field] = browser.find_element(By.ID,field)
    for field in senderFields:
        elementsSenderData[field] = browser.find_element(By.ID,field)


    #Enter user input to its field
    elementsPackageSize[parcelSize].click()


    for i in range(0,len(communicators)):
        for field in fields[i]:
            if data[i][field] != "":
                elementsCommunicator[i][field].send_keys(data[i][field])

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

    btnNewOrder = browser.find_element(By.XPATH,"/html/body/div[3]/section/div/div/div[1]/div/div/div/div[7]/div/div[1]/a")
    browser.get(btnNewOrder.get_attribute("href"))
    time.sleep(3)
    browser.close()
    data[0].clear()
    data[1].clear()
    exit = False if "n" ==input("Exit y/n ?") else True
