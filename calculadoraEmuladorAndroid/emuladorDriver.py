import os
from appium import webdriver

class emuladorDriver():
    dir = '../evidencias/'

    def criarPastaEvidencia(self, nPasta):
        try:
            d = dir + nPasta
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
        except:
            print('Verifique se o diretório há arquivos.')

    def gerarScreenshot(self, nPasta, nEvidencia):
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