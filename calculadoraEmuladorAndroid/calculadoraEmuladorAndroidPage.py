from time import sleep
from calculadoraEmuladorAndroid import emuladorAndroidVariables, emuladorBasePage
from calculadoraEmuladorAndroid.emuladorDriver import emuladorDriver

v = emuladorAndroidVariables
p = emuladorBasePage.BasePage
d = emuladorDriver

dirSoma = '../evidencias/Soma'
dirSubtracao = '../evidencias/Subtracao'
dirMultiplicacao = '../evidencias/Multiplicao'
dirDivisao = '../evidencias/Divisao'

class calculadoraAndroidPage():
    def soma(self):
        d.criarPastaEvidencia(self,dirSoma)
        p.clicar(self,"id",v.btnUm)
        p.clicar(self, "id", v.btnDois)
        p.clicar(self, "id", v.btnTres)

        p.clicar(self,"id",v.btnSom)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        p.clicar(self,"id",v.btnIgual)

        d.gerarScreenshot(self,dirSoma,"Ev1")
        p.validarTexto(self,"id",v.txtResultado,"579")
        sleep(1)
        p.clicar(self,"id",v.btnLimp)

    def subtracao(self):
        d.criarPastaEvidencia(self, dirSubtracao)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSete)
        p.clicar(self, "id", v.btnNove)

        p.clicar(self,"id",v.btnSub)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        p.clicar(self, "id", v.btnIgual)

        d.gerarScreenshot(self, dirSubtracao, "Ev1")
        p.validarTexto(self,"id",v.txtResultado,"123")
        sleep(1)
        p.clicar(self, "id", v.btnLimp)

    def multiplicao(self):
        d.criarPastaEvidencia(self, dirMultiplicacao)
        p.clicar(self, "id", v.btnTres)
        p.clicar(self, "id", v.btnUm)

        p.clicar(self, "id", v.btnMult)

        p.clicar(self, "id", v.btnUm)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnIgual)

        d.gerarScreenshot(self, dirMultiplicacao, "Ev1")
        p.validarTexto(self, "id", v.txtResultado, "310")
        sleep(1)
        p.clicar(self, "id", v.btnLimp)

    def divisao(self):
        d.criarPastaEvidencia(self, dirDivisao)
        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnDiv)

        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnIgual)

        d.gerarScreenshot(self, dirDivisao, "Ev1")
        p.validarTexto(self,"id",v.txtResultado,"Impos. dividir por 0")
        sleep(1)
        p.clicar(self, "id", v.btnDel)

        p.clicar(self, "id", v.btnQuatro)

        p.clicar(self, "id", v.btnIgual)

        d.gerarScreenshot(self, dirDivisao, "Ev2")
        p.validarTexto(self, "id", v.txtResultado, "225")
        p.clicar(self, "id", v.btnLimp)