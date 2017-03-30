'''
Created on 30/03/2017

@author: Rachappa
'''
from selenium import webdriver
import time
from lib2to3.tests.support import driver
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://twitter.com/signup?lang=en")
    driver.find_element_by_id("full-name").send_keys("rachappa")
    driver.find_element_by_id("email").send_keys("rachappahalinge@gmail.com")
    driver.find_element_by_id("password").send_keys("rach222")
    element=driver.find_element_by_class_name("js-current-language")
    time.sleep(2)
    e1=element.click()
    time.sleep(2)
    driver.find_element_by_xpath().click()
    driver.find_element_by_id()
    
    
    
    
