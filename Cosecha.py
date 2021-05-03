class claseCosecha:
    __lista = []
    def __init__(self, lista = []):
        self.__lista = lista
    def cargarBi(self, lista):
        self.__lista = lista
    def getLista(self):
        return self.__lista
    def test1(self):
        print(self.__lista)