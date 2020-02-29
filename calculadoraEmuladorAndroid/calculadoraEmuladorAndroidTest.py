import unittest
from appium import webdriver
from calculadoraEmuladorAndroid import calculadoraEmuladorAndroidPage

p = calculadoraEmuladorAndroidPage.calculadoraAndroidPage

class calculadoraAndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(12)

    def tearDown(self):
        self.driver.quit()

    def test1_Soma(self):
        p.soma(self)

    def test2_Subtracao(self):
        p.subtracao(self)

    def test3_Multiplicacao(self):
        p.multiplicao(self)

    def test4_Divisao(self):
        p.divisao(self)

if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(calculadoraAndroidTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
