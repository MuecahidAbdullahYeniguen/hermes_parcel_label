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

NOW_SENDER = "-"
EOIPNUT = "#"


receiverInput = list()
senderInput = list()
input = [receiverInput, senderInput]

elementsPackageSize = list()
elementsReceiverData = list()
elementsSenderData = list()
elementsCommunicator = [elementsReceiverData, elementsSenderData]

# Read input of user for parcel labe
filepath = r'C:\Users\MJ\Desktop\python_automation\user_input.txt'
fp = open(filepath, "r")
fileContent = fp.readlines()
for i in range(0, len(fileContent)):
    fileContent[i] = fileContent[i].replace("\n", "")

parceSize = fileContent.pop(0)
fileContent.pop(0)
i = 0
for value in fileContent:
    if NOW_SENDER in value:
        i += 1
        continue
    if EOIPNUT in value:
        break
    input[i].append(value)

print(input)
print("----------------")

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        match j:
            case 0:
                if len(input[i][j].split(" ")) == 2:
                    print("Name1")
                    print(input[i][j].split(" ")[1])
                    data[i][fields[i][j]] = input[i][j].split(" ")[0]
                    data[i][fields[i][j+1]] = input[i][j].split(" ")[1]
                else:
                    print("Name2")
                    data[i][fields[i][j+1]] = input[i][j]
            case 1:
                if "strasse" in input[i][j]:
                    data[i][fields[i][j+1]] = input[i][j]
            case 2:
                if re.match(r"^[0-9]{1,2}$", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
            case 3:
                if re.match(r"\d{5}", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
            case 4:
                if re.match(r"^[A-Za-z]+$", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
            case 5:
                if re.match(r"[A-Za-z]+\@[A-Za-z]+\.[A-Za-z]+", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
                elif re.match(r"\d{12}", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
            case 6:
                if re.match(r"\d{12}", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]
                elif re.match(r"[A-Za-z]+\@[A-Za-z]+\.[A-Za-z]+", input[i][j]):
                    data[i][fields[i][j+1]] = input[i][j]


for com in data:
    for element in com.items():
        print(element)

"""

for i in range(0,len(userInputReading)):
    if i < int(len(userInputReading)/2):
        userInput[0].append(userInputReading[(i)])
    else:
        userInput[1].append(userInputReading[(i)])
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
    for i in range(0,MAX_COUNT_FIELDS):
        elementsCommunicator[i][i].send_keys(userInput[i][i])

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
