from time import sleep
from selenium.webdriver.common.by import By
import appium.webdriver.common.touch_action

class BasePage():
    def clicar(self, tipoEl, el):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element(By.ID,el).click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element(By.NAME,el).click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element(By.XPATH,el).click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            self.driver.find_element(By.CLASS_NAME,el).click()
        elif tipoEl == "LINK" or tipoEl.__eq__("link"):
            self.driver.find_element(By.LINK_TEXT,el).click()
        elif tipoEl == "TAG" or tipoEl.__eq__("tag"):
            self.driver.find_element(By.TAG_NAME,el).click()
        elif tipoEl == "PARTIAL" or tipoEl.__eq__("partial"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT,el).click()
        elif tipoEl == "CSS" or tipoEl.__eq__("css"):
            self.driver.find_element(By.CSS_SELECTOR,el).click()

    def validarTexto(self,tipoEl,el,texto):
        sleep(1)
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            txt = self.driver.find_element(By.ID,el).text
            assert texto == txt
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            txt = self.driver.find_element(By.NAME,el).text
            assert texto == txt
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            txt = self.driver.find_element(By.XPATH,el).text
            assert texto == txt
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            txt = self.driver.find_element(By.CLASS_NAME,el).text
            assert texto == txt
        elif tipoEl == "LINK" or tipoEl.__eq__("link"):
            txt = self.driver.find_element(By.LINK_TEXT, el).text
            assert texto == txt
        elif tipoEl == "TAG" or tipoEl.__eq__("tag"):
            txt = self.driver.find_element(By.TAG_NAME, el).text
            assert texto == txt
        elif tipoEl == "PARTIAL" or tipoEl.__eq__("partial"):
            txt = self.driver.find_element(By.PARTIAL_LINK_TEXT, el).text
            assert texto == txt
        elif tipoEl == "CSS" or tipoEl.__eq__("css"):
            txt = self.driver.find_element(By.CSS_SELECTOR, el).text
            assert texto == txt
        sleep(1)

    def scrollDown(self):
        sleep(1)
        touch = appium.TouchAction(self.driver)
        touch.press(x=290, y=840).move_to(x=292, y=191).release().perform()
        sleep(1)