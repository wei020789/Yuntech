from selenium import webdriver
import time

url = 'https://webapp.yuntech.edu.tw/AAXCCS/CourseSelectionRegister.aspx'
account = "學號"
pd = "密碼"
number = '課號'


driverPath = "./chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get(url)
#login
driver.find_element_by_id('pLoginName').send_keys(account)
driver.find_element_by_id('pLoginPassword').send_keys(pd)
driver.find_element_by_id('LoginSubmitBtn').click()
while(1):
    driver.get(url)
    driver.find_element_by_id('ContentPlaceHolder1_CurrentSubjTextBox').send_keys(number)
    driver.find_element_by_id('ContentPlaceHolder1_QueryButton').click()
    driver.find_element_by_id('ContentPlaceHolder1_QueryCourseGridView_SelectCheckBox_0').click()
    driver.find_element_by_id('ContentPlaceHolder1_Label7').click()
    driver.find_element_by_id('ContentPlaceHolder1_Label8').click()
    driver.find_element_by_id('ContentPlaceHolder1_Label11').click()
    driver.find_element_by_id('CloseButton').click()
    time.sleep(1)
    # break
    
    
