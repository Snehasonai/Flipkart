import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class order(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def OpenPage(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")

    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")

    def Enter_Username(self, username1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH", username1)

    def Enter_password(self, password1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password1)

    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("loginbutton1_XPATH")

    def over_to_profile(self):
            time.sleep(5)
            WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")))
            e = self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
            a = ActionChains(self.driver)
            a.move_to_element(e)
            a.perform()
            time.sleep(5)

    def Click_order(self):
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[4]/a[1]/div[1]").click()
        time.sleep(5)

    def Click_ontheway(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[2]/label/div").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div[2]/label/div").click()
        time.sleep(5)

    def Click_delivered(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[3]/label/div").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div[3]/label/div").click()
        time.sleep(5)

    def Click_cancelled(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[4]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div[4]/label/div").click()
        time.sleep(5)


    def Click_Returned(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[5]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[2]/div[5]/label/div").click()
        time.sleep(5)

    def Click_Last(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[2]/div/div[3]/div[1]/div/div[3]/div[2]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[2]/label/div").click()
        time.sleep(5)

    def Click_2022(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[3]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[3]/label/div").click()
        time.sleep(5)

    def Click_2021(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[4]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[4]/label/div").click()
        time.sleep(5)

    def Click_2020(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[5]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[5]/label/div").click()
        time.sleep(5)

    def Click_2019(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[6]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[6]/label/div").click()
        time.sleep(5)




    def Click_older(self):
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[7]/label/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div[3]/div[1]/div/div[3]/div[7]/label/div").click()
        time.sleep(5)



