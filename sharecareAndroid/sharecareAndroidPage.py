from time import sleep
from sharecareAndroid import baseTest,basePage, sharecareAndroidVariables

t = baseTest
p = basePage
v = sharecareAndroidVariables

dirRegistreSe = '../evidencias/RegistreSe'
dirLogin = '../evidencias/Login'

#class sharecareAndroidPage():

def registreSe(self,nome,sobrenome,email,dtNasc,sexo,cep,senha):
        t.criarPastaEvidencia(self,dirRegistreSe)

        self.driver.find_element_by_id(v.btnEntrar).is_displayed()
        self.driver.find_element_by_xpath(v.btnRegistreSe).click()
        self.driver.find_element_by_xpath(v.txtVoceMoraNoBrasilSim).is_displayed()
        self.driver.find_element_by_xpath(v.btnVoceMoraNoBrasilSim).click()
        self.driver.find_element_by_xpath(v.btnAltereoPaisEmQueResideOK).click()
        sleep(2)
        self.driver.find_element_by_xpath(v.txtCrieUmaConta).is_displayed()
        self.driver.hide_keyboard()

        self.driver.find_element_by_id(v.cpNome).send_keys(nome)
        self.driver.find_element_by_id(v.cpSobrenome).send_keys(sobrenome)
        self.driver.find_element_by_id(v.cpEmail).send_keys(email)
        if sexo == "M" or sexo.__eq__("m"):
            self.driver.find_element_by_id(v.cbSexoM).click()
        elif sexo == "F" or sexo.__eq__("f"):
            self.driver.find_element_by_id(v.cbSexoF).click()
        t.gerarScreenshot(self,dirRegistreSe,"Ev1")
        self.driver.find_element_by_id(v.cpCEP).send_keys(cep)
        self.driver.find_element_by_id(v.cpSenha).send_keys(senha)
        p.scrollDown(self)
        self.driver.find_element_by_id(v.cpConfirmarSenha).send_keys(senha)
        self.driver.find_element_by_id(v.cbEuConcordo).click()
        t.gerarScreenshot(self,dirRegistreSe,"Ev2")
        self.driver.find_element_by_xpath(v.btnCriar).click()
        t.gerarScreenshot(self,dirRegistreSe,"Ev3")

def login(self,email,senha):
        t.criarPastaEvidencia(self, dirLogin)

        self.driver.find_element_by_id(v.btnEntrar).click()
        self.driver.find_element_by_id(v.btnEntrar).click()
        sleep(1)
        self.driver.find_element_by_xpath(v.txtInformeUmemailValido).is_displayed()
        self.driver.find_element_by_xpath(v.txtInformeSuaSenha).is_displayed()
        t.gerarScreenshot(self,dirLogin,"Ev1")
        sleep(1)

        self.driver.find_element_by_xpath(v.cpLoginEmail).send_keys(email)
        self.driver.find_element_by_xpath(v.cpLoginSenha).send_keys("share")
        sleep(1)
        t.gerarScreenshot(self, dirLogin, "Ev2")

        self.driver.find_element_by_id(v.btnEntrar).click()
        self.driver.find_element_by_xpath(v.txtOcorreuUmErro).is_displayed()
        self.driver.find_element_by_xpath(v.txtEmailOuSenhaInvalidos).is_displayed()
        sleep(1)
        t.gerarScreenshot(self, dirLogin, "Ev3")

        self.driver.find_element_by_id(v.btnFechar).click()
        self.driver.find_element_by_xpath(v.cpLoginSenha).send_keys(senha)
        sleep(1)
        t.gerarScreenshot(self, dirLogin, "Ev4")

        self.driver.find_element_by_id(v.btnEntrar).click()
        self.driver.implicitly_wait(18)
        self.driver.find_element_by_id(v.btnProximo).click()
        self.driver.find_element_by_id(v.btnProximo).click()
        self.driver.find_element_by_id(v.btnPermitir).click()
        self.driver.find_element_by_id(v.btnPermitir).click()
        self.driver.find_element_by_id(v.btnPermitir).click()
        self.driver.find_element_by_id(v.btnPermitir).click()
        self.driver.find_element_by_id(v.btnPermitir).click()
        t.gerarScreenshot(self, dirLogin, "Ev5")
        self.driver.find_element_by_id(v.btnProximo).click()
        sleep(1)

        self.driver.find_element_by_xpath(v.lblPaginaInicial).is_displayed()
        self.driver.find_element_by_xpath(v.lblMonitore).is_displayed()
        self.driver.find_element_by_xpath(v.lblDescubra).is_displayed()
        self.driver.find_element_by_xpath(v.lblRealize).is_displayed()
        self.driver.find_element_by_xpath(v.lblVoce).is_displayed()
        t.gerarScreenshot(self, dirLogin, "Ev6")

        self.driver.find_element_by_xpath(v.lblVoce).click()
        self.driver.find_element_by_id(v.iconConfiguracoes).click()
        t.gerarScreenshot(self, dirLogin, "Ev7")
        self.driver.find_element_by_xpath(v.btnConfiguracoesSair).click()
        self.driver.find_element_by_xpath(v.btnSair).click()
        sleep(1)
        self.driver.find_element_by_xpath(v.btnRegistreSe).is_displayed()
        t.gerarScreenshot(self, dirLogin, "Ev8")