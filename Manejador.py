from Camion import claseCamion
from Cosecha import claseCosecha
import csv
class claseManejador:
    __listaCamion = []
    __listaDia = []
    __cosecha = None
    __archi1 = None
    __archi2 = None
    def __init__(self, lista=[], listaDia = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'],
                 cosecha = claseCosecha(), archi1 = open('ListaCamion.csv'),archi2 = open('ListaCosecha.csv')):
        self.__listaCamion = lista
        self.__listaDia = listaDia
        self.__cosecha = cosecha
        self.__archi1 = archi1
        self.__archi2 = archi2
    def crearListaCamion(self): #crea la lista a partir del archivo
        band = True
        reader = csv.reader(self.__archi1, delimiter = ';')
        for fila in reader:
            if(band == True):
                band = False
            else:
                unCamion = claseCamion(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
                self.__listaCamion.append(unCamion)
    def crearListaCosecha(self):    #crea la lista cosecha a partir del archivo
        reader = csv.reader(self.__archi2, delimiter = ';')
        band = [True, True]
        indice = [0]
        listaTotal = []
        for fila in reader:
            listaParcial = []
            if(band[0] == True):
                band[0] = False
            else:
                for columna in fila:
                    if(band[1] == True):
                        band[1] = False
                    else:
                        if(float(columna)>self.__listaCamion[indice[0]].getTara()):
                            toneladas = round(float(columna)-self.__listaCamion[indice[0]].getTara(), 2)
                            listaParcial.append(toneladas)
                        else: print('ERROR: la tara es mayor al peso transportado')
                band[1] = True
                listaTotal.append(listaParcial)
                indice[0]+=1
        self.__cosecha.cargarBi(listaTotal)
        print('DATO: lista cargada')
    def crearListaCosechaManual(self):  #crea la lista a través del ingreso manual
        listaTotal = []
        i = 0
        band = False
        xdia = 0
        for i in range(20): #seteo de la lista
            listaParcial = []
            for j in range(7):
                listaParcial.append(0.0)
            listaTotal.append(listaParcial)
        print('INGRESE LOS DATOS: \n(ID del camión, día, peso del camión)\nDATO: para finalizar, ID inválida')
        id = int(input('ID del camionero: '))
        if(id>=1 and id<=20):
            while (id >= 1 and id <= 20):
                dia = str(input('Día: '))
                kg = float(input('Peso del camión(kg): '))
                for i in range(len(self.__listaDia)):
                    if (str(self.__listaDia[i]) == dia.lower()):
                        xdia = i
                if ((kg / 1000) > self.__listaCamion[id].getTara()):
                    listaTotal[id - 1][xdia] = round((kg / 1000) - self.__listaCamion[id].getTara(), 2)
                else:
                    print('ERROR: los kilogramos ingresados es menor a la tara del camión')
                id = int(input('ID del camionero: '))
                i = 0
            self.__cosecha.cargarBi(listaTotal)
        else: print('ERROR:id inválida')
    def muestraKilos(self, id): #muestra los kilos descargados de un camión
        acum = 0.0
        lista = self.__cosecha.getLista()
        for i in range(7):
            acum+=lista[id][i]
        acum = round(acum, 2)
        return acum
    def muestraDia(self, dia):  #muestras los datos de los camioneros
        cabeza = """\
        +-------------------------------------------------------------------+
        | Patente               Conductor                 Cantidad de kilos |
        |-------------------------------------------------------------------|\
        """
        cuerpo = """\
        | {:9}              {:20}              {:6}kg |\
        """
        cola = """\
        |-------------------------------------------------------------------|
        +-------------------------------------------------------------------+\
        """
        print(cabeza)
        lista = self.__cosecha.getLista()
        for i in range(len(self.__listaCamion)):
            print(cuerpo.format(self.__listaCamion[i].getPatente(), self.__listaCamion[i].getNom(), lista[i][dia]*1000))
        print(cola)
    def test1(self):    #muestra la lista que contiene los datos de los camioneros
        print('Mostrar lista camion: ')
        for i in range(len(self.__listaCamion)):
            print('{}'.format(self.__listaCamion[i].test()))
    def test2(self):    #muestra la lista de cosecha
        print('Mostrar Lista cosecha: ')
        self.__cosecha.test1()