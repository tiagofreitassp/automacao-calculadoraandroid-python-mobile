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
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSete)
        p.clicar(self, "id", v.btnNove)

        p.clicar(self,"id",v.btnSub)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        p.clicar(self, "id", v.btnIgual)

        p.validarTexto(self,"id",v.txtResultado,"123")
        sleep(1)
        p.clicar(self, "id", v.btnLimp)

    def multiplicao(self):
        p.clicar(self, "id", v.btnTres)
        p.clicar(self, "id", v.btnUm)

        p.clicar(self, "id", v.btnMult)

        p.clicar(self, "id", v.btnUm)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnIgual)
        p.validarTexto(self, "id", v.txtResultado, "310")
        sleep(1)
        p.clicar(self, "id", v.btnLimp)

    def divisao(self):
        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnDiv)

        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnIgual)

        p.validarTexto(self,"id",v.txtResultado,"Impos. dividir por 0")
        sleep(1)
        p.clicar(self, "id", v.btnDel)

        p.clicar(self, "id", v.btnQuatro)

        p.clicar(self, "id", v.btnIgual)

        p.validarTexto(self, "id", v.txtResultado, "225")
        p.clicar(self, "id", v.btnLimp)