'''
So jon's iphone's home button broke and the only way unlock it is if he has a notification, 
so i cobbled together some really disgusting selenium code (see below) to send him an email 
from a throw away gmail account every 5 minutes  

its 1:30 am right now so Im just going to leave this running all night and see what happens
'''
    
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

numSent = 0
while(True):
    driver = webdriver.Chrome()
    driver.get("https://www.gmail.com")

    # address:  sailormoonwalkhome@gmail.com
    # pw:       kibae123

    addressField = driver.find_element_by_id("identifierId")
    addressField.send_keys('sailormoonwalkhome')
    addressField.send_keys(Keys.ENTER)

    time.sleep(2)

    pwField = driver.find_element_by_name("password")
    # pwField = pwFieldList[0]
    pwField.send_keys('kibae123')
    pwField.send_keys(Keys.ENTER)

    time.sleep(5)
    
    body = driver.find_element_by_tag_name("body")
    body.send_keys("c") # shortcut for compose
    time.sleep(5)
    try:
        toBox = driver.find_element_by_id(":9s")
        toBox.send_keys('jonlockm.11@gmail.com')
        subjectBox = driver.find_element_by_name("subjectbox")
        subjectBox.send_keys('esketit')
        bodyBox = driver.find_element_by_id(":af")
        bodyBox.send_keys('this is a notification')
        sendButton = driver.find_element_by_id(":90")
        sendButton.send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        driver.close()
        print('failed to send email, restarting chrome')
        continue

    numSent = numSent+1
    print("sent {} emails so far".format(numSent))
    driver.close()
    time.sleep(60*5) # send an email every 5 minutes