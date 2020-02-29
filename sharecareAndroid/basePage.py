from time import sleep
from appium.webdriver.common.touch_action import TouchAction

def scrollDown(self):
        sleep(1)
        touch = TouchAction(self.driver)
        touch.press(x=290, y=840).move_to(x=292, y=191).release().perform()
        sleep(1)