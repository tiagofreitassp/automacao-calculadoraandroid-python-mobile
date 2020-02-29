import unittest
from appium import webdriver
from calculadoraEmuladorAndroid import calculadoraEmuladorAndroidPage, emuladorDriver

d = emuladorDriver.emuladorDriver
p = calculadoraEmuladorAndroidPage.calculadoraAndroidPage

class calculadoraAndroidTest(unittest.TestCase):
    def setUp(self):
        d.criarDriver(self)

    def tearDown(self):
        d.fecharDriver(self)

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
