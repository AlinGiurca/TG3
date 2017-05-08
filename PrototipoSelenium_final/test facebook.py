#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

def runSeleniumDriver():
	chromedriver = "C:/Users/Roberto/Desktop/chromedriver" #Donde tenga el chromedriver
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome()
	driver.maximize_window()	
	return driver 

def login(driver):
	driver.get("http://www.facebook.com")

for i in range (1,3):

	driver = runSeleniumDriver()
	login(driver)

#Obtención de los elementos de la página.
	driver.find_element_by_name("firstname").send_keys("Pedro") #.send_keys rellena el campo que hemos localizado.
	time.sleep(1)
	driver.find_element_by_name("lastname").send_keys("Ramirez")
	time.sleep(1)
	driver.find_element_by_name("reg_email__").send_keys("pedro.ramir"+str(i)+"@hotmail.com")
	time.sleep(1)
	driver.find_element_by_name("reg_email_confirmation__").send_keys("pedro.ramir"+str(i)+"@hotmail.com")
	time.sleep(1)
	driver.find_element_by_name("reg_passwd__").send_keys("1a|2b@")
	time.sleep(1)
	driver.find_element_by_id("day").send_keys("27")
	time.sleep(1)
	driver.find_element_by_id("month").send_keys("Sep")
	time.sleep(1)
	driver.find_element_by_id("year").send_keys("1991")
	time.sleep(1)
	driver.find_element_by_id("u_0_h").click()
	time.sleep(1)
	driver.find_element_by_id("u_0_l").click()
	time.sleep(1)
	i= i+1	


