import  re
class claseCamion:
    __id = 0
    __nom = ''  #nombre del conductor
    __patente = ''  #patente del camión
    __marca = ''    #marca del camión
    __tara = 0.0    #peso de camión vacío en toneladas
    def __init__(self, id, nom, patente, marca, tara):
        if(id >= 1 and id <= 20):   #verifica que la id sea correcta
            if(re.match('^[a-z\ ]{3,20}$', nom.lower())): #verifica que el nombre sea correcto
                if(re.match('^[a-z\ 0-9]{7,9}', patente.lower())):  #verifica que la patente sea correcta
                    if(re.match('^[a-z\_\-\.\ ]{3,30}', marca.lower())):    #verifica la marca sea correcta
                        if(tara > 0):
                            self.__id = id
                            self.__nom = nom
                            self.__patente = patente
                            self.__marca = marca
                            self.__tara = tara
                        else: print('ERROR: tara inválida')
                    else: print('ERROR: marca inválida')
                else: print('ERROR: patente inválida')
            else: print('ERROR: nombre inválido')
        else: print('ERROR: id inválido')
    def test(self):
        return '{}-{}-{}-{}-{}'.format(self.__id, self.__nom, self.__patente, self.__marca, self.__tara)
    def getTara(self):
        return self.__tara
    def getPatente(self):
        return self.__patente
    def getNom(self):
        return self.__nom