# automacao-calculadoraandroid-python-mobile
Script de automacao para realizar calculos basicos na calculadora do Android usando Python, Selenium, Appium e Unittest.

### Cobertura dos testes:  ###

* Realizar calculos basicos na calculadora do Android no emulador.

* Realizar calculos basicos na calculadora do Android no smartphone.

## Tecnologias:
* [Python 3.8+](https://www.python.org/)
* [Unittest](https://docs.python.org/3/library/unittest.html)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)
* [PyPI](https://pypi.org/project/selenium/)

## Dependências:
* Selenium
* OS
* Appium-Python-Client
* Time
* DocX
* Utilize o pip install para instalar via terminal os drivers dos navegadores.

## Instruções de execução:

###  - Plataforma
*Importante:

O projeto foi criado para executar no MacOS. Mas pode receber adaptacoes para executar no Windows e Linux caso nao execute bem fora do MacOS.

Recomendado utilizar o PyCharm, mas pode usar o Eclipse IDE ou Visual Studio Code.

Utilize a versão 2 do Appim, pois as anteriores foram depreciadas e não possuem suporte do Desenvolvedor.

###  - Fluxo
*Descricao: Este script ira executar calculos basicos como Soma, Subtracao, Multiplicacao e Divisao.

###  - Massas
*Descricao: 
Nao e necessario criar massas por enquanto.

###  - Evidencias
*Descricao:
Apos a execucao as imagens de evidencias sao armazenadas na pasta evidencias.

Para visualizar as evidencias no documento pode usar o MS Office Word ou o LibreOffice

###  - Inicializar a automação
*Descricao:

Abrir uma das classes ***Test.py no PyCharm.

No caso para executar num smartphone, abra a classe Mobile Driver e altere o valor no campo "deviceName".