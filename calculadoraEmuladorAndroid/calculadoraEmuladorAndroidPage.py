from time import sleep
from calculadoraEmuladorAndroid import emuladorAndroidVariables, emuladorBasePage

v = emuladorAndroidVariables
p = emuladorBasePage.BasePage

class calculadoraAndroidPage():
    def soma(self):
        p.clicar(self,"id",v.btnUm)
        p.clicar(self, "id", v.btnDois)
        p.clicar(self, "id", v.btnTres)

        p.clicar(self,"id",v.btnSom)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        p.clicar(self,"id",v.btnIgual)

        p.validarTexto(self,"id",v.txtResultado,"579")
        sleep(1)
        p.clicar(self,"id",v.btnLimp)

    def subtracao(self):
        self.driver.find_element_by_id(v.btnCinco).click()
        self.driver.find_element_by_id(v.btnSete).click()
        self.driver.find_element_by_id(v.btnNove).click()

        self.driver.find_element_by_id(v.btnSub).click()

        self.driver.find_element_by_id(v.btnQuatro).click()
        self.driver.find_element_by_id(v.btnCinco).click()
        self.driver.find_element_by_id(v.btnSeis).click()

        self.driver.find_element_by_id(v.btnIgual).click()
        txt = self.driver.find_element_by_id(v.txtResultado).text
        assert "123" == txt
        sleep(1)
        self.driver.find_element_by_id(v.btnLimp).click()

    def multiplicao(self):
        self.driver.find_element_by_id(v.btnTres).click()
        self.driver.find_element_by_id(v.btnUm).click()

        self.driver.find_element_by_id(v.btnMult).click()

        self.driver.find_element_by_id(v.btnUm).click()
        self.driver.find_element_by_id(v.btnZero).click()

        self.driver.find_element_by_id(v.btnIgual).click()
        txt = self.driver.find_element_by_id(v.txtResultado).text
        assert "310" == txt
        sleep(1)
        self.driver.find_element_by_id(v.btnLimp).click()

    def divisao(self):
        self.driver.find_element_by_id(v.btnNove).click()
        self.driver.find_element_by_id(v.btnZero).click()
        self.driver.find_element_by_id(v.btnZero).click()

        self.driver.find_element_by_id(v.btnDiv).click()

        self.driver.find_element_by_id(v.btnQuatro).click()

        self.driver.find_element_by_id(v.btnIgual).click()
        txt = self.driver.find_element_by_id(v.txtResultado).text
        assert "225" == txt
        sleep(1)
        self.driver.find_element_by_id(v.btnLimp).click()