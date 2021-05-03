from Manejador import claseManejador
from Camion import claseCamion
from Menu import claseMenu
import os
def test():
    band = False
    while not band:
        print('1.CrearCamión - 2.Crear lista camión - 3. Crear lista cosecha\n(para el 3 es necesario el 2)')
        op = int(input('Opción: '))
        manejador = claseManejador()
        if (op == 1):
            id = int(input('ID: '))
            nom = str(input('Nombre:'))
            patente = str(input('Patente: '))
            marca = str(input('Marca: '))
            tara = float(input('Tara: '))
            camion = claseCamion(id, nom, patente, marca, tara)
            print('{}'.format(camion.test()))
        elif (op == 2):
            manejador.crearListaCamion()
            manejador.test1()
        elif (op == 3):
            print('CREAR LISTA COSECHA\n1. Carga manual\n2. Cargar el archivo')
            op = int(input('Opción: '))
            if(op == 1):
                manejador.crearListaCosechaManual()
                manejador.test2()
            elif(op == 2):
                manejador.crearListaCosecha()
                manejador.test2()
            else: print('ERROR: opción inválida')
        else: band = True
if __name__ == '__main__':
    if(str(input('¿Testear?: ')).lower() == 'si'):
        test()
    else:
        #datos
        manejador = claseManejador()
        salir = False
        menu = claseMenu()
        #procedimientos iniciales
        manejador.crearListaCamion()
        manejador.crearListaCosecha()
        #procedimientos
        while not salir:
            os.system('cls')
            print('----MENU----\n1. Mostrar kilos descargados\n2. Lista del día\n3. Salir')
            op = int(input('Opción: '))
            os.system('cls')
            menu.menu(op)
            salir = op == 3