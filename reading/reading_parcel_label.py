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

filledFields = {
    "firstname": "",
    "lastname": "",
    "street": "",
    "houseNumber": "",
    "zipCode": "",
    "city": "",
    "email": "",
    "phone": ""
}

fields = ["firstname", "lastname", "street",
          "houseNumber", "zipCode", "city", "email", "phone"]
communicators = ["receiver", "sender"]
packageSizes = ["HP", "S", "M", "L", "XL", "XXL"]
receiverData = ["receiverAddressFirstname", "receiverAddressLastname", "receiverAddressStreet",
                "receiverAddressHouseNumber", "receiverAddressZipCode", "receiverAddressCity", "receiverEmail", "receiverPhone"]
senderData = ["senderAddressFirstname", "senderAddressLastname", "senderAddressStreet",
              "senderAddressHouseNumber", "senderAddressZipCode", "senderAddressCity", "senderEmail", "senderPhone"]
NOW_SENDER = "-"
EOIPNUT = "#"


elementsPackageSize = list()
elementsReceiverData = list()
elementsSenderData = list()
elementsCommunicator = [elementsReceiverData, elementsSenderData]

# Read input of user for parcel labe
filepath = r'C:\Users\MJ\Desktop\python_automation\user_input.txt'
fp = open(filepath, "r")
input = fp.readlines()

for i in range(0, len(input)):
    input[i] = input[i].replace("\n", "").replace(" ", "")
    print(input[i])
print("----------------")
parcelSize = input.pop(0)
input.pop(0)


for i in range(0, len(input)):
    match i:
        case 0:
            if len(input[i].split(" ")) == 2:
                print("NAME1")
            else:
                print("NAME2")
        case 1:
            if "strasse" or "straße" in input[i]:
                print("STRASSE")
        case 2:
            if re.match(r"^[0-9]{1,2}$", input[i]):
                print("HOUSENUMBER")
        case 3:
            if re.match(r"\d{5}", input[i]):
                print("ZIPCODE")
        case 4:
            if re.match(r"^[A-Za-z]+$", input[i]):
                print("STADDDTT")
        case 5:
            if re.match(r"[A-Za-z]+\@[A-Za-z]+\.[A-Za-z]+", input[i]):
                print("EMIALL")
            elif re.match(r"\d{12}", input[i]):
                print("TELEFON")
        case 6:
            if re.match(r"\d{12}", input[i]):
                print("TELEFON")
            elif re.match(r"[A-Za-z]+\@[A-Za-z]+\.[A-Za-z]+", input[i]):
                print("EMIALL")

    


"""
parcelSize = fp.readline()
fp.readline()
name = fp.readline().replace("\n", "").split(" ")
if len(name) == 2:
    filledFields["firstname"] = name[0]
    filledFields["lastname"] = name[1]
else:
    filledFields["lastname"] = name[0]

filledFields["street"] = "".join([val for val in fp.readline() if val.isalpha()])
filledFields["houseNumber"] = "".join([val for val in fp.readline() if val.isnumeric()])
filledFields["zipCode"] = "".join([val for val in fp.readline() if val.isnumeric()])
filledFields["city"] = "".join([val for val in fp.readline() if val.isalpha()])
filledFields["email"] = fp.readline().rstrip("\n")
filledFields["phone"] = "".join([val for val in fp.readline() if val.isnumeric()])

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

browser.close()"""
