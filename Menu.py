from Manejador import claseManejador
import os
class claseMenu:
    __op = 0
    __manejador = None
    def __init__(self, op = 0, manejador = claseManejador()):
        self.__op = op
        self.__manejador = manejador
    def menu(self, op):
        if(op == 1):    #mostrar la cantidad total descargada de un camión
            id = int(input('ID del camionero: '))
            if(id>=1 and id<=20):
                print('Kilos descargados: {}kg'.format(self.__manejador.muestraKilos(id-1)*1000))
                os.system('pause')
            else: print('ERROR: id inválida')
        elif(op == 2):  #mostrar lista día
            print('Elegir día:\n1. Lunes\t2. Martes\t3. Miércoles\t4. Jueves\t5. Viernes\t6. Sábado\t7. Domingo')
            dia = int(input('Día: '))
            if(dia>=1 and dia<=7):
                self.__manejador.muestraDia(dia-1)
                os.system('pause')
            else: print('ERROR: día inválida')
        elif(op == 3):
            print('DATO: finalizando...')
        else: print('ERROR: opción incorrecta')