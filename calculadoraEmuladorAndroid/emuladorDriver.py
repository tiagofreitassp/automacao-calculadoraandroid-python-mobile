import os
from time import sleep
from appium import webdriver

class emuladorDriver():
    dir = '../evidencias/'

    def criarPastaEvidencia(self, nPasta):
            d = nPasta
            if os.path.exists(d) == True:
                print("Diretório já existe")
                os.rmdir(d)
                print('Diretório apagado')
                os.makedirs(d)
                print('Diretório recriado')
            else:
                print("Diretório não existe")
                os.makedirs(d)
                print('Diretório criado')

    def gerarScreenshot(self, nPasta, nEvidencia):
        sleep(1)
        self.driver.get_screenshot_as_file(nPasta + "/" + nEvidencia + ".png")

    def criarDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(12)

    def fecharDriver(self):
        self.driver.quit()