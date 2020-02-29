class BasePage():
    def clicar(self, tipoEl, el):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            self.driver.find_element_by_id(el).click()
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            self.driver.find_element_by_name(el).click()
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            self.driver.find_element_by_xpath(el).click()
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            self.driver.find_element_by_class_name(el).click()

    def validarTexto(self,tipoEl,el, texto):
        if tipoEl == "ID" or tipoEl.__eq__("id"):
            txt = self.driver.find_element_by_id(el).text
            assert texto == txt
        elif tipoEl == "NAME" or tipoEl.__eq__("name"):
            txt = self.driver.find_element_by_name(el).text
            assert texto == txt
        elif tipoEl == "XPATH" or tipoEl.__eq__("xpath"):
            txt = self.driver.find_element_by_xpath(el).text
            assert texto == txt
        elif tipoEl == "CLASS" or tipoEl.__eq__("class"):
            txt = self.driver.find_element_by_class_name(el).text
            assert texto == txt