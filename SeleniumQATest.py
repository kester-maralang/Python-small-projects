from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


############################################
#######################################
#Script Configuration
############################################
#######################################

#Username
user = "myemailaddress"
#Password
pwd = "mypassword"
#Instantiate Chrome Driver
driverpath = "C:\\Users\\kmaralang\\PycharmProjects\\QASelenium\\drivers\\chromedriver.exe"
driver = webdriver.Chrome(driverpath)
#Open up test environment
driver.get("https://devsiteurl.com/")

############################################
#######################################
#End Script Configuration
############################################
#######################################


###METHODS
#Enter Username
elem = driver.find_element_by_id("username")
elem.send_keys(user)

#Enter Password
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)

#Press submit button for login
time.sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()

#Click on Portfolios, then go to the Portfolios tab
#Then browse to other Sub tabs

time.sleep(3)
portfolios_link = driver.find_element_by_link_text('Portfolios').click()

#Sub tabs
time.sleep(3)
portfolio_link = driver.find_element_by_link_text('Portfolio').click()

time.sleep(3)
dashboard_link = driver.find_element_by_link_text('Dashboard').click()

time.sleep(3)
analytics_link = driver.find_element_by_link_text('Analytics').click()

time.sleep(3)
obligors_link = driver.find_element_by_link_text('Obligors').click()

time.sleep(3)
industries_link = driver.find_element_by_link_text('Industries').click()

time.sleep(3)
country_link = driver.find_element_by_link_text('Country').click()

time.sleep(3)
collateral_link = driver.find_element_by_link_text('Collateral').click()

#Click on Assumptions, then go to the Assumptions tab
time.sleep(3)
assumptions_link = driver.find_element_by_link_text('Assumptions').click()

#Click on OLM, then go to the OLM tab
time.sleep(3)
olm_link = driver.find_element_by_link_text('OLM').click()

#Closes the program
#time.sleep(10)
#driver.quit()
